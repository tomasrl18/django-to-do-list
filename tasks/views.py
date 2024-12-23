from django.shortcuts import render, redirect
from .models import Task

# Mostrar todas las tareas
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Añadir una nueva tarea
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(title=title)
        return redirect('task_list')
    return render(request, 'tasks/add_task.html')

# Marcar una tarea como completada
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')

# Eliminar una tarea
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')
