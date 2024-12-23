from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Mostrar todas las tareas
def task_list(request):
    tasks = Task.objects.all().order_by('priority')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Añadir una nueva tarea
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        priority = request.POST['priority']
        Task.objects.create(title=title, priority=priority)
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

def task_toggle(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed  # Cambiar el estado de 'completed'
    task.save()
    return redirect('task_list')