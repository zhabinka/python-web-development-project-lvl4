from django.db import models

class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
