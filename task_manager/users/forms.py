from django import forms
from django.core.exceptions import ValidationError
from task_manager.users.models import User

class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def clean_first_name(self):
        name = self.cleaned_data['first_name']
        if len(name) > 10:
            raise ValidationError('Длина не должна превышать 10 символов')

        return name
