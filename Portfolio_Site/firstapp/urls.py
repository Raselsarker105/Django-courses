# urls.py
from django.urls import path
from .views import view_resume, upload_resume, view_skills, add_skill, contact_information, contact
from . import views

urlpatterns = [
    path('view_resume/', views.view_resume, name='view_resume'),
    path('upload_resume/', views.upload_resume, name='upload_resume'),
    path('view_skills/', views.view_skills, name='view_skills'),
    path('add_skill/', views.add_skill, name='add_skill'),
    path('contact/', views.contact, name='contact_form'),
    path('contact_info/', views.contact_information, name='contact_info'),
]
