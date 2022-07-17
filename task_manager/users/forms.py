from django import forms

class AddUserForm(forms.Form):
    email = forms.CharField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
