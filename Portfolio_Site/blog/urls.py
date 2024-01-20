from django.urls import path
from . import views
from .views import BlogListView, blog_detail, BlogCreateView

urlpatterns = [
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_detail/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog_create/', BlogCreateView, name='blog_create'),
]
