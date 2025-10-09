# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Example paths, aap apni views ke hisab se add/change kar sakte hain
    path('projects/', views.ProjectListView.as_view(), name='project-list'),
    path('tasks/', views.TaskListView.as_view(), name='task-list'),
]