# app/post/views.py

# Django modules
from django.shortcuts import render

# Locals

# Create your views here.

def home_page(request):
	return render(request, 'app/post/index.html')