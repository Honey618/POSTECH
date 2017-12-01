
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
            url(r'^$', views.main, name='main'),
			url(r'^logout/$', auth_views.logout, {'next_page' : '/'}),
            ]
