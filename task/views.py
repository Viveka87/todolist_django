from django.shortcuts import render,get_object_or_404,redirect
from .models import Notes

# Create your views here.
def index(request):
    if request.method=='POST':
        title=request.POST.get('title')
        if title:
            Notes.objects.create(title=title)  
        return redirect('index') 
    all_notes=Notes.objects.all() .order_by('created_at')
    return render(request,'tasks/view_task.html',{'task_list':all_notes})


def edit_task(request,pk):
    notes=get_object_or_404(Notes,pk=pk)   

    if request.method=='POST':
        new_title=request.POST.get('title') 
        new_status=request.POST.get('completed')

        notes.title=new_title
        notes.completed=new_status
        notes.save()

        return redirect('index')
    
    return render(request,'tasks/edit_task.html',{'notes_res':notes})


def delete_task(request, pk):
    del_note = get_object_or_404(Notes, pk=pk)
    del_note.delete()
    return redirect('index')
