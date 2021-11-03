from django.shortcuts import render, redirect
from .models import Project
# This is where we will create business logic.
# 'projects/projects.html' means that django will find templates folder in projects folder to get html files.
# Create your views here.
from django.http import HttpResponse
from .forms import ProjectForm




def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'projects/projects.html',context)

def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'projects/single-project.html',{'project':projectObj})

def createProject(request):
    form = ProjectForm()

    if request.method=="POST":
        form = ProjectForm(request.POST) # Creates a new form object
        if form.is_valid(): # check if all fields match or not
            form.save() # Form gets saved
            return redirect('projects') # User is redirected to main projects page.
    context = {'form':form}
    return render(request,"projects/project_form.html",context=context)

def updateProject(request,pk):
    project = Project.objects.get(id=pk) # get the project with the id of the primary key requested
    form = ProjectForm(instance=project) # get the object of the ProjectForm instance and store it in form.

    if request.method == "POST":
        form = ProjectForm(request.POST,instance=project) # get the object of that instance.
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request,"projects/project_form.html",context=context)

def deleteProject(request,pk):
    project = Project.objects.get(id=pk)
    if request.method=='POST':
        project.delete()
        return redirect('projects')
    context = {'object':project}
    return render(request,'projects/delete_template.html',context)