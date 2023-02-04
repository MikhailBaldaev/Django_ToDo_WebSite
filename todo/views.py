from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from todo.models import Todo


# Create your views here.

@login_required
def home(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        new_todo = Todo(user=request.user, name=task)
        new_todo.save()

    all_tasks = Todo.objects.filter(user=request.user)
    context = {'todos': all_tasks}
    return render(request, 'todo/todo.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username):
            messages.error(request, 'Username already exists')
            return redirect('register')

        if len(password) <= 3:
            messages.error(request, 'Password should not be less then 4 characters')
            return redirect('register')

        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()

        messages.success(request, 'User successfully created! Please, log in now.')
        return redirect('login')

    context = {}
    return render(request, 'todo/register.html', context)


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        validate_user = authenticate(username=username, password=password)

        if validate_user is not None:
            login(request, validate_user)
            return redirect('home')
        else:
            messages.error(request, 'Wrong username or password')
            return redirect('login')

    context = {}
    return render(request, 'todo/login.html', context)

@login_required
def delete_task(request, name):
    task = Todo.objects.get(user=request.user, name=name)
    task.delete()
    return redirect('home')

@login_required
def update_task(request, name):
    task = Todo.objects.get(user=request.user, name=name)
    task.status = True
    task.save()
    return redirect('home')


def logoutf(request):
    logout(request)
    return redirect('login')

