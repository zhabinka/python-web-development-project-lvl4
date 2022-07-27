from django.db import models
from task_manager.users.models import User
from task_manager.statuses.models import Status

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    author = models.ForeignKey(User, related_name='author', on_delete=models.PROTECT)
    executor = models.ForeignKey(User, related_name='executor', on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
