from django.urls import path, include
from task_manager.users import views


app_name = 'users'

urlpatterns = [
    # path('', views.index),
    path('', views.index, name='index'),
    path('add/', include('django.contrib.auth.urls')),
    # path('create/', views.addUser),
    path('create/', views.SignUpView.as_view(), name='create'),
]
