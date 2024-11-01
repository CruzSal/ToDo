from django.shortcuts import render, redirect, get_object_or_404
from ToDoApp.models import Task
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#First is an example of a class based view,
#Second is an example of a function based view
#To change between them, change urls.py

class TaskListView(ListView):
    model = Task
    template_name = 'ToDo/task_list.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'ToDo/add_task.html'
    fields = ['title']
    success_url = reverse_lazy('task_list')

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'ToDo/edit_task.html'
    fields = ['title', 'isCompleted']
    success_url = reverse_lazy('task_list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'ToDo/delete_task.html'
    success_url = reverse_lazy('task_list')

def task_list(request):
    context = {}
    tasks = Task.objects.all()
    context.update({'tasks': tasks})
    return render(request, 'ToDo/task_list.html', context)
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('task_list')
    return render(request, 'ToDo/add_task.html')

#Task.objects.create(title=title) is equivalent to:
#   task = Task(title=title)
#   task.save()
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.title = request.POST.get('title',task.title)
        task.isCompleted = request.POST.get('isCompleted') == 'on'  
        task.save()
        return redirect('task_list')
    return render(request, 'ToDo/edit_task.html', {'task': task})
#def edit_task(request, task_id):
#    task = Task.objects.get(id=task_id)

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'ToDo/delete_task.html', {'task': task})
#def delete_task(request, task_id):
#   task = Task.objects.get(id=task_id)
#task_id instead of pk and get_object_or_404(Task) instead of Task.objects.get