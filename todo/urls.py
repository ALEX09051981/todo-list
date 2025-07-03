from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tags/', views.tag_list, name='tag-list'),
    path('task/add/', views.task_create, name='task-add'),
    path('task/<int:pk>/update/', views.task_update, name='task-update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task-delete'),
    path('task/<int:pk>/toggle/', views.toggle_task, name='task-toggle'),
    path('tag/add/', views.tag_create, name='tag-add'),
    path('tag/<int:pk>/update/', views.tag_update, name='tag-update'),
    path('tag/<int:pk>/delete/', views.tag_delete, name='tag-delete'),
]