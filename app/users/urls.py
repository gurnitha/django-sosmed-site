# app/users/views.py

# Django modules
from django.urls import path

# Locals
from app.users import views

# App name
app_name = 'users'

# Create your path here.


urlpatterns = [
    path('register/', views.register_page, name='register'),
]
