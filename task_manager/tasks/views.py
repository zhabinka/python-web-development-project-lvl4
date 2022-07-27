from django.shortcuts import render
from django.http import HttpResponseRedirect
from task_manager.tasks.forms import CreateTaskForm
from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.statuses.models import Status


def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})


def createTask(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tasks')
    else:
        form = CreateTaskForm()

    return render(request, 'tasks/create.html', {'form': form})


def editTask(request, pk):
    task = Task.objects.get(id=pk)
    form = CreateTaskForm(instance=task)

    if request.method == 'POST':
        author = User.objects.get(id=request.POST.get('author'))
        executor = User.objects.get(id=request.POST.get('executor'))
        status = Status.objects.get(id=request.POST.get('status'))

        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.author = author
        task.executor = executor
        task.status = status

        task.save()
        # form = CreateTaskForm(request.POST)
        # form.save()
        return HttpResponseRedirect('/tasks')

    return render(request, 'tasks/create.html', {'form': form, 'task': task})


def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    form = CreateTaskForm(instance=task)
    if request.method == 'POST':
        task.delete()
        return HttpResponseRedirect('/tasks')

    return render(request, 'tasks/delete.html', {'task': task, 'form': form})
