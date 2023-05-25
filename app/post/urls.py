# app/post/views.py

# Django modules
from django.urls import path

# Locals
from app.post import views

# App name
app_name = 'post'

# Create your path here.


urlpatterns = [
    path('', views.home_page, name='home'),
]
