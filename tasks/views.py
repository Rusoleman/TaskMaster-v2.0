from django.shortcuts import get_object_or_404, redirect, render

from .models import Task
from .forms import TaskForm


def getTasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})

def createTask(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form':TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.save()
            return redirect('tasks')
        except:
            return render(request, 'create_task.html', {
            'form':TaskForm
            })

def updateTask(request, task_id):
    task = get_object_or_404(Task, pk = task_id)
    if request.method == 'GET':
        form = TaskForm(instance = task)
        return render(
            request, 'task_detail.html', 
            {
                'task':task,
                'form':form
            }
        )
    else:
        try:
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(
                request, 
                'task_detail.html', 
                {
                    'task':task,
                    'form':form,
                    'error':"An error has occurred while updating your Task!"
                }
            )

def deleteTask(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('tasks')