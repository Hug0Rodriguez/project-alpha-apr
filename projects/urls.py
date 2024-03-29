from django.urls import path
from projects import views

urlpatterns = [
    path("", views.list_projects, name="list_projects"),
    path("<int:id>/", views.show_project, name="show_project"),
    path("create/", views.create_project, name="create_project"),
]
