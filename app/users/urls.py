# app/users/views.py

# Django modules
from django.urls import path
from django.contrib.auth import views as auth
# Locals
from app.users import views

# App name
app_name = 'users'

# Create your path here.


urlpatterns = [
    path('register/', views.register_page, name='register'),
    path('login/', auth.LoginView.as_view(
        template_name='app/users/login.html'), name='login'),
]
