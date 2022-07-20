from django.shortcuts import render
from django.views.generic import ListView
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
    session = request.session
    print(session)
    return render(request, 'users/index.html', { 'users': users})

# class ListUser(ListView):
#     model = User


from django.contrib.auth.models import User

def addAuthUser(request):
    # Создайте пользователя и сохраните его в базе данных
    user = User.objects.create_user('xz', 'jopa@crazymail.com', 'mypassword')

    # Обновите поля и сохраните их снова
    user.first_name = 'John'
    user.last_name = 'Citizen'
    user.save()
