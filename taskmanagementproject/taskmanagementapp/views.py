from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import TaskManagementItem

# Create your views here.
def taskmanagementView(request):
    items = TaskManagementItem.objects.all()
    return render(request, 'taskmanagement.html', {'all_items': items})

def addTaskView(request):
    x = request.POST['content']
    new_item = TaskManagementItem(content=x)
    new_item.save()
    return HttpResponseRedirect('/taskmanagement/')

def deleteTaskView(request, i):
    # x = request.POST['id']
    x = i
    item = TaskManagementItem.objects.get(id=x)
    item.delete()
    return HttpResponseRedirect('/taskmanagement/')