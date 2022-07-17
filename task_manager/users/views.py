from django.shortcuts import render
from django.http import HttpResponseRedirect
from task_manager.users.forms import AddUserForm
from task_manager.users.models import User


def addUser(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            try:
                User.objects.create(**form.cleaned_data)
                return HttpResponseRedirect('/users/')
            except:
                form.add_error(None, 'Error')
    else:
        form = AddUserForm()

    return render(request, 'users/create.html', { 'form': form })
