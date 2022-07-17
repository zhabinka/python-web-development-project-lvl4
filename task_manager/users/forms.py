from django import forms
from task_manager.users.models import User

class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')
