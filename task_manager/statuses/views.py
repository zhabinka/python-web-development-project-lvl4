from django.shortcuts import render
from django.http import HttpResponseRedirect
from task_manager.statuses.forms import CreateStatusForm
from task_manager.statuses.models import Status


def index(request):
    statuses = Status.objects.all()
    print(statuses.first())
    return render( request, 'statuses/index.html', {'statuses': statuses})


def createStatus(request):
    if request.method == 'POST':
        form = CreateStatusForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/statuses')
    else:
        form = CreateStatusForm()

    return render(request, 'statuses/create.html', {'form': form})


def deleteStatus(request, pk):
    status = Status.objects.get(id=pk)
    form = CreateStatusForm(instance=status)
    if request.method == 'POST':
        status.delete()
        return HttpResponseRedirect('/statuses')

    return render(request, 'statuses/delete.html', {'status': status, 'form': form})



def editStatus(request, pk):
    status = Status.objects.get(id=pk)
    form = CreateStatusForm(instance=status)

    if request.method == 'POST':
        status.name = request.POST.get('name')
        status.save()
        return HttpResponseRedirect('/statuses')
    else:
        return render(request, 'statuses/edit.html', {'status': status, 'form': form})

