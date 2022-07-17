from django.shortcuts import render
from django.http import HttpResponseRedirect
from task_manager.users.forms import AddUserForm
from task_manager.users.models import User


def addUser(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/users')
    else:
        form = AddUserForm()

    return render(request, 'users/create.html', { 'form': form })

def index(request):
    users = User.objects.all()
    return render(request, 'users/index.html', { 'users': users})
