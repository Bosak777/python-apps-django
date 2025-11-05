from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("notice/", views.notice, name="notice"),
    path("search/", views.search, name="search"),
    path("profile/", views.profile, name="profile"),

]
