from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import *

# LOGINAPP views.py

# Create your views here.
def index(request):
	return render(request, 'loginapp/index.html')

def register(request):
	did_register = User.objects.register(request)

	if did_register[0]:
		request.session['user'] = {
			'id' : did_register[1].id,
			'first_name' : did_register[1].first_name,
			'last_name' : did_register[1].last_name,
			'email' : did_register[1].email
		}
		return redirect(reverse('success'))
	else:
		print_messages(request, did_register[1])
		return redirect(reverse('loginapp-index'))

def login(request):
	did_login = User.objects.login(request)
	if did_login[0]:
		request.session['user'] = {
			'id' : did_login[1].id,
			'first_name' : did_login[1].first_name,
			'last_name' : did_login[1].last_name,
			'email' : did_login[1].email
		}
		return redirect(reverse('success'))
	else:
		print_messages(request, did_login[1])
		return redirect(reverse('loginapp-index'))

def success(request):
	if not 'user' in request.session:
		return redirect(reverse('loginapp-index'))
	return redirect(reverse('friends-index'))

def logout(request):
	request.session.pop('user')
	return redirect(reverse('loginapp-index'))

def print_messages(request, message_list):
	for message in message_list:
		messages.add_message(request, messages.INFO, message)