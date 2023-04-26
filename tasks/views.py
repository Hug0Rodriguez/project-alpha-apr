from django.shortcuts import render, redirect
from tasks.models import TaskForm, Task
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = TaskForm()
    return render(request, "tasks/create_task.html", {"form": form})


@login_required
def show_my_tasks(request):
    context = {
        "my_tasks": Task.objects.filter(assignee=request.user),
    }
    return render(request, "tasks/show_my_tasks.html", context)
