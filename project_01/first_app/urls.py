

# first_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses),
    path('about/', views.about),
    path('', views.homes)
]