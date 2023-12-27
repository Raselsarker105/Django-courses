from django.shortcuts import render
from Tasks.models import TaskModel

def home(request):
    data = TaskModel.objects.all()
    print(data)
    return render(request, 'home.html', {'data': data})
    #return render(request, 'home.html')