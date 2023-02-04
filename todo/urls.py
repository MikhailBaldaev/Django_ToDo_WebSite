
from django.contrib import admin
from django.urls import path

from todo.views import home, register, loginpage, delete_task, update_task, logoutf


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', loginpage, name='login'),
    path('delete/<str:name>/', delete_task, name='delete'),
    path('update/<str:name>/', update_task, name='update'),
    path('logout', logoutf, name='logout'),

]
