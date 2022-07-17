from django.urls import path
from django.views.generic import TemplateView
from task_manager.users.views import addUser


app_name = 'users'

urlpatterns = [
    path('', TemplateView.as_view(template_name='users/index.html')),
    path('create/', addUser),
]
