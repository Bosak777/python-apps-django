from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path("", views.reiwa_year, name="reiwa_year"),
]
