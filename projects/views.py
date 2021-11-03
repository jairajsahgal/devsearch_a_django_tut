from django.shortcuts import render
from .models import Project
# This is where we will create business logic.
# 'projects/projects.html' means that django will find templates folder in projects folder to get html files.
# Create your views here.
from django.http import HttpResponse




def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'projects/projects.html',context)

def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'projects/single-project.html',{'project':projectObj})

def createProject(request):
    context = {}
    return render(request,"projects/project_form.html",context=context)


