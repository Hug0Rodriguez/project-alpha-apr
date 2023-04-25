from django.urls import path
from projects import views

urlpatterns = [
    path("", views.list_projects, name="list_projects"),
]
