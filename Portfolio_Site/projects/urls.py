from django.contrib import admin
from django.urls import path, include
from . import views
from .views import add_category, addProject, DetailProjectView, allProject


app_name = 'projects'
urlpatterns = [
    path('category/', add_category, name='add_category'),
    path('add_project/', addProject, name='add_project'),
    path('all_project/', allProject, name='all_project'),
    #path('details/<int:id>/', views.DetailProjectView.as_view(), name='detail_project'),
]
