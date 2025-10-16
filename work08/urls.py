from django.urls import path
from . import views

urlpatterns = [
    path('index_top/', views.memo, name="memo"),
    path('add_memo/', views.add_memo, name="add_memo"),
]
