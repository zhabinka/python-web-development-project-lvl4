from django.urls import path
from task_manager.statuses import views


app_name = 'statuses'

urlpatterns = [
    path('', views.index),
    path('create/', views.createStatus),
    path('<int:pk>/delete/', views.deleteStatus),
    path('<int:pk>/update/', views.editStatus),
]
