
from django.http import HttpResponse

def home(request):
    # Your view logic here
    return HttpResponse("Home page successfully created!")

def contact(request):
    # Your view logic here
    return HttpResponse("Contact page successfully created!")