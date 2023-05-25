# app/users/views.py

# Django modules
from django.shortcuts import render

# Locals
from app.users.forms import RegisterUserForm

# Create your views here.

def register_page(request):
	form = RegisterUserForm()
	context = {'form':form}
	return render(request, 'app/users/register.html', context)