
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homes(request):
    return HttpResponse("This is first_app__?__home page successfully created!")

def courses(request):
    return HttpResponse("This is first_app__?__Courses page successfully created!")

def about(request):
    return HttpResponse("This is first_app__?__About page successfully created!")