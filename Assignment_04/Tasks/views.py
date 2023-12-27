from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.
def add_task (request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task')
    else:
        task_form = forms.TaskForm()
    return render(request, 'add_task.html', {'form': task_form})


def edit_task(request, id):
    task = models.TaskModel.objects.get(pk=id)
 
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            # Update the existing task instance with the submitted form data
            task.title = task_form.cleaned_data['title']
            task.description = task_form.cleaned_data['description']
            task.is_completed = task_form.cleaned_data['is_completed']
            task.assign_date = task_form.cleaned_data['assign_date']
            task.categories.set(task_form.cleaned_data['categories'])
            task.save()
 
            return redirect('homepage')  
 
    else:
        task_form = forms.TaskForm(instance=task)
 
    return render(request, 'add_task.html', {'form': task_form})


def delete_task(request, id):
    task = models.TaskModel.objects.get(pk=id)  
    task.delete()
    return redirect('homepage')  
 
    




