from django.urls import path
from task_manager.users import views


app_name = 'users'

urlpatterns = [
    path('', views.index),
    path('create/', views.addUser),
]
