from __future__ import unicode_literals
from django.db import models
from ..loginapp.models import User

# FRIENDS models.py

# Create your models here.
class FriendManager(models.Manager):
	def get_friends(self, user):
		friends = User.objects.filter(friend__friends__user=user)
		return friends

	def make_friends(self, user1, user2):
		relationship = Friend.objects.get(user=user1)
		relationship.friends.add(Friend.objects.get(user=user2))

	def remove_friend(self, user1, user2):
		relationship = Friend.objects.get(user=user1)
		relationship.friends.remove(Friend.objects.get(user=user2))


class Friend(models.Model):
	user = models.OneToOneField(User)
	friends = models.ManyToManyField('self', symmetrical=True)

	objects = FriendManager()