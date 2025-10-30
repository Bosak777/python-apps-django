from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index_todo"),
    path('add_task/', views.todo_task, name="add_ta"),
]
