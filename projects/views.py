from django.shortcuts import render, redirect
from .models import Project
from django.contrib.auth.decorators import login_required

from .models import Project, Tag
# This is where we will create business logic.
# 'projects/projects.html' means that django will find templates folder in projects folder to get html files.
# Create your views here.
from django.http import HttpResponse
from .forms import ProjectForm
from .utils import searchProjects, paginateProjects


def projects(request):
    projects, search_query = searchProjects(request)

    custom_range, projects = paginateProjects(request, projects, 6)

    context = {'projects': projects, "search_query": search_query, 'custom_range': custom_range}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'projects/single-project.html', {'project': projectObj})


@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST,
                           request.FILES)  # Creates a new form object # request.FILES for processing files in backend
        if form.is_valid():  # check if all fields match or not
            project = form.save(commit=False)  # Form gets saved
            project.owner = profile
            project.save()
            return redirect('account')  # User is redirected to main projects page.

    context = {'form': form}
    return render(request, "projects/project_form.html", context=context)


@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)  # get the project with the id of the primary key requested
    form = ProjectForm(instance=project)  # get the object of the ProjectForm instance and store it in form.

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)  # get the object of that instance.
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form': form}
    return render(request, "projects/project_form.html", context=context)


@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'delete_template.html', context)
