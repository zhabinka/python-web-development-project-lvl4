from django.urls import path
from task_manager.tasks import views


app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.createTask),
    path('<int:pk>/update/', views.editTask),
    path('<int:pk>/delete/', views.deleteTask),
]
