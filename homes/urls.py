from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_list, name="home_list"),
    path("add/", views.home_create, name="home_create"),
    path("<int:pk>/edit/", views.home_update, name="home_update"),
    path("<int:pk>/delete/", views.home_delete, name="home_delete"),
]