from django.urls import path
from ToDoApp.views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.create_task, name='add_task'),
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),

    #Paths for Class Based Views
    #path('', TaskListView.as_view(), name='task_list'),
    #path('add/', TaskCreateView.as_view(), name='add_task'),
    #path('edit/<int:pk>/', TaskUpdateView.as_view(), name='edit_task'),
    #path('delete/<int:pk>/', TaskDeleteView.as_view(), name='delete_task'),
]