from django.urls import path
from . import views

urlpatterns = [
    path('index_todo/', views.todo, name="todo"),
    path('todo_list/', views.todo_list, name="todo_list"),
]
