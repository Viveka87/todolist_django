from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('index')
    
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/index.html', {'tasks': tasks})

def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    
    if request.method == 'POST':
        new_title = request.POST.get('title')
        if new_title:
            task.title = new_title
            task.save()
            return redirect('index')
            
    return render(request, 'tasks/edit_task.html', {'task': task})

def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect('index')