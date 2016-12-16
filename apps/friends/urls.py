from django.conf.urls import url
from . import views

# FRIENDS urls.py

urlpatterns = [
	url(r'^$', views.index, name='friends-index'),
	url(r'^friends$', views.friends, name='friends-dashboard'),
	url(r'^user/(?P<id>\d+)$', views.user, name='display-user'),
	url(r'^user/add/(?P<id>\d+)$', views.add_friend, name='add-friend'),
]