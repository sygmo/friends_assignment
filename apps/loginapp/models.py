from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
	def register(self, request):
		errors = self.check_inputs(request)

		if len(errors) > 0:
			return (False, errors)

		# hash the password
		pwhash = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())

		new_user = User.objects.create(
			first_name=request.POST['first_name'],
			last_name=request.POST['last_name'],
			email=request.POST['email'],
			pwhash=pwhash
		)
		new_user.save()
		# save to the db
		return (True, new_user)

	def login(self, request):
		try:
			user = User.objects.get(email=request.POST['email'])
			# get the user
			guess_hash = bcrypt.hashpw(request.POST['password'].encode('utf-8'), user.pwhash.encode('utf-8'))
			# rehash the pw
			if guess_hash == user.pwhash:
				return (True, user)

		except ObjectDoesNotExist:
			pass

		return (False, ["Email/password combo doesn't match."])

	def check_inputs(self, request):
		errors = []
		if len(request.POST['first_name']) < 2 or len(request.POST['last_name']) < 2:
			errors.append("First Name/Last Name is required and must be at least two characters.")
		if not EMAIL_REGEX.match(request.POST['email']):
			errors.append("Not a valid email address.")
		users = User.objects.filter(email=request.POST['email'])
		if len(users) > 0:
			errors.append("That email is taken.")
		if len(request.POST['password']) < 8 or request.POST['password'] != request.POST['password_confirm']:
			errors.append("Passwords must match and be at least 8 characters long.")

		return errors


class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.CharField(max_length=45)
	pwhash = models.CharField(max_length=60)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

	objects = UserManager()