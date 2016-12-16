from django.conf.urls import url
from . import views

# LOGINAPP urls.py

urlpatterns = [
	url(r'^$', views.index, name='loginapp-index'),
	url(r'^register$', views.register, name='register'),
	url(r'^login$', views.login, name='login'),
	url(r'^logout$', views.logout, name='logout'),
	url(r'^success$', views.success, name='success')
]