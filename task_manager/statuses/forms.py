from django import forms
from task_manager.statuses import models


class CreateStatusForm(forms.ModelForm):
    class Meta:
        model = models.Status
        fields = ('name',)

