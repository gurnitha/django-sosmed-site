# app/users/views.py

# Django modules
from django.shortcuts import render, redirect

# Locals
from app.users.forms import RegisterUserForm

# Create your views here.

def register_page(request):

	# If form is submited and the method is POST
	if request.method == 'POST':
		# Get instances from the form, and hold them in the form_var variable
		form_var = RegisterUserForm(request.POST)
		# If form_var is valid
		if form_var.is_valid():
			# Save the form_var
			form_var.save()
			# Redirect the user to the login page
			return redirect('users:login') # not yet created

	# If the submited form method is not POST 
	else:
		form = RegisterUserForm()
	
	context = {'form':form}
	return render(request, 'app/users/register.html', context)