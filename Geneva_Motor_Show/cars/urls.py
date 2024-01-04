from django.contrib import admin
from django.urls import path, include
from .views import BuyCarView
from . import views
urlpatterns = [
    path('add/', views.AddPostCreateView.as_view(), name='add_post'),
    path('details/<int:id>/', views.DetailCarView.as_view(), name='detail_car'),
    path('car/<int:id>/', views.BuyCarView.as_view(), name='Buy_car'),
]