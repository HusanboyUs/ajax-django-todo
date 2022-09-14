from django.urls import path
from api import views

urlpatterns = [
    path('tasks/', views.TodoList.as_view(), name='task-list'),
    path('tasks-create/', views.CreateTask, name='task-create'),
    path('tasks-update/<str:pk>/', views.UpdateTask, name='task-update'),
    path('tasks-delete/<str:pk>/', views.DeleteTask, name='task-delete'),
]
