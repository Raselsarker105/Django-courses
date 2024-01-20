from django.urls import path
from . import views
from .views import UserRegistrationView, UserLoginView, UserAccountUpdateView, change_password

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', UserAccountUpdateView.as_view(), name='profile'),
    path('change_password/', views.change_password, name='change_password'),
]
