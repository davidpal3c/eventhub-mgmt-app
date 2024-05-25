from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm, ResetPasswordForm
from django.conf import settings
from django.core.mail import send_mail



def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('events:list-events')
		else:
			messages.success(request, ("There Was An Error Logging In, Try Again..."))	
			return redirect('login')	


	else:
		return render(request, 'userauth/login.html', {})
	

def logout_user(request):
	logout(request)
	messages.success(request, ("You Were Logged Out..."))	
	return redirect('events:list-events')



def register_user(request):
	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)

			recipient_email = [request.POST.get('email')]

			subject = 'Welcome to EventHub'
			message = f'Hi {username}, thank you for registering in EventHub.ca'
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email]
			send_mail(subject, message, email_from, recipient_email, fail_silently=True)

			messages.success(request, ("Registration Successful!"))
			return redirect('events:list-events')
		
	else:
		form = RegisterUserForm()


	return render(request, 'userauth/register_user.html', 
			   {'form': form})


def reset_password(request):

	form = ResetPasswordForm()

	context = {
		"form": form
	}

	return render(request, 'userauth/reset_password.html', context)