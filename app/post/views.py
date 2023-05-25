# app/post/views.py

# Django modules
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Locals

# Create your views here.

@login_required()
def home_page(request):
	return render(request, 'app/post/index.html')

def about_page(request):
	return render(request, 'app/post/about.html')

@login_required()
def account_page(request):
	return render(request, 'app/post/account.html')