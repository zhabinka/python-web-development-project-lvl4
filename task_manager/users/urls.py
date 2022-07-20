from django.urls import path, include
from task_manager.users import views


app_name = 'users'

urlpatterns = [
    # path('', views.index),
    path('', views.index, name='users'),
    path('create/', views.addUser),
    path('add/', include('django.contrib.auth.urls')),
]
