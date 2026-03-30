from django.shortcuts import render, redirect
from .models import Task

def index(request):
    # Fetch all tasks from MySQL, ordered by newest first
    tasks = Task.objects.all().order_by('-created_at')
    
    # Handle adding a new task (POST request)
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('index')

    return render(request, 'tasks/index.html', {'tasks': tasks})