from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from ..loginapp.models import User
from django.core.exceptions import ObjectDoesNotExist

# FRIENDS view.py

def index(request):
	if not 'user' in request.session:
		return redirect(reverse('loginapp-index'))
	else:
		return redirect(reverse('friends-dashboard'))

def friends(request):
	try:
		friends = Friend.objects.get_friends(request.session['user'].get('id'))
		users = User.objects.all().exclude(id=request.session['user'].get('id'))
		context = {
			"friends" : friends,
			"users" : users
		}
		return render(request, "friends/friends.html", context)
	
	except ObjectDoesNotExist:
		pass
		
	users = User.objects.all().exclude(id=request.session['user'].get('id'))
	#print "USERS: ", users	
	context = {
		"users" : users
	}
	return render(request, "friends/friends.html", context)

def user(request, id):
	user = User.objects.get(id=id)
	if request.method == "GET":
		return render(request, 'friends/user.html', { 'user' : user })
	return redirect(reverse('friends-dashboard'))

def add_friend(request, id):
	Friend.objects.make_friends(get_user(request.session['user'].get('id')), get_user(id))
	return redirect(reverse('friends-dashboard'))

def get_user(id):
	user = User.objects.get(id=id)
	#print "USER: ", user
	return user