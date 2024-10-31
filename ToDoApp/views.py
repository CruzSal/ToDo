from django.shortcuts import render
from ToDoApp.models import Task
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.
from django.urls import reverse_lazy

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

""" def list_of_tasks(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'list_tasks.html', context)

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task(title=title, description=description)
        task.save()
        return render(request, 'create_task.html', {'task': task})
    return render(request, 'create_task.html')

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task.title = title
        task.description = description
        task.save()
        return render(request, 'edit_task.html', {'task': task})
    return render(request, 'edit_task.html', {'task': task})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return render(request, 'delete_task.html', {'task': task}) """