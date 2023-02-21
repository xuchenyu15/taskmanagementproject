from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
import datetime

# Create your views here.
def taskmanagementView(request):
    items = TaskManagementItem.objects.all()
    return render(request, "taskmanagement.html", {"all_items": items})


def addTaskView(request):
    x = request.POST["content"]
    new_item = TaskManagementItem(content=x)
    new_item.save()
    return HttpResponseRedirect("/taskmanagement/")


def deleteTaskView(request, i):
    # x = request.POST['id']
    x = i
    item = TaskManagementItem.objects.get(id=x)
    item.delete()
    return HttpResponseRedirect("/taskmanagement/")


def editTaskView(request, i):
    item = TaskManagementItem.objects.get(id=i)
    return render(request, "edittask.html", {"item": item})


def updateTaskView(request, i):
    item = TaskManagementItem.objects.get(id=i)
    content = request.POST["content"]
    status = request.POST["status"]
    item.set_content(content)
    item.set_status(status)
    item.set_created_at(datetime.datetime.now())
    item.save()
    return HttpResponseRedirect("/taskmanagement/")


def searchTaskView(request):
    query = request.POST["query"]
    results = {"all_items": TaskManagementItem.objects.filter(content__icontains=query)}
    return render(request, "taskmanagement.html", results)


def homeView(request):
    return render(request, "home.html")
