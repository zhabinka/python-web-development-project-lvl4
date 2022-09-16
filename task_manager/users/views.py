from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.http import HttpResponseRedirect
from task_manager.users.forms import AddUserForm
from task_manager.users.models import User

from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/create.html'

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
