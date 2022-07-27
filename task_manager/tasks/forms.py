from django import forms
from task_manager.tasks import models


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ('title', 'description', 'author',
                'executor', 'status')
