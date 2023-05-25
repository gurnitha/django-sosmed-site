# app/users/views.py

# Django modules
from django.shortcuts import render

# Locals

# Create your views here.

def register_page(request):
	return render(request, 'app/users/register.html')