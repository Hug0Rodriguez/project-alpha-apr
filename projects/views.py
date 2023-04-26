from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project, ProjectForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def list_projects(request):
    context = {
        "projects": Project.objects.filter(owner=request.user),
    }
    return render(request, "projects/list_projects.html", context)


@login_required
def show_project(request, id):
    project = get_object_or_404(Project, id=id)
    context = {"project": project}
    return render(request, "projects/show_project.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()

    context = {"form": form}
    return render(request, "projects/create_project.html", context)
