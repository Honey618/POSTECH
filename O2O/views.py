# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .models import Poster, User
from .forms import UserForm, PictureUploadForm, FeedbackForm, EditForm
from .parser.detect import *
from .parser.parser import *

from .calendar.quickstart import *

# def main(request):
# 	return render(request, 'main.html')

def myimages(request):
	from .models import Poster
#	posters = Poster.objects.filter(id=user)
	# posters = Poster.objects.all()

	username = request.session.get('username')
	
	if not username:
		return redirect('/')	


	user = User.objects.get(username = username)
	posters = Poster.objects.filter(user=user)


	for poster in posters:
		attract = Poster.objects.filter(eventname=poster.eventname)
		poster.attract = len(attract)


	return render(request, 'myimages.html', {'users': username, 'posters': posters})


def main(request):
	from .models import Poster
	posters = Poster.objects.all()

	users = request.session.get('username')

	return render(request, 'main.html', {'users': users, 'posters': posters })

def sign_up(request):
	username = None;
	message = "";

	if request.method == 'GET':
		return redirect('/')

	else:
		user_form = UserForm(data=request.POST)

		if user_form.is_valid():
			try:
				user = user_form.sign_up()
			except Exception as e:
				message = "This ID Already Exists"
			else:
				pass
			finally:
				return redirect('/?message=%s' % message)
			

			# if user:
			# 	return redirect('/')

			# else:
			# 	# TODO: 에러 처리 해줘야함
			# 	return redirect('/')
		return redirect('/')

def login(request):
	username = None;
	message = ""

	if request.method == 'GET':

		return redirect('/')
	else :
		user_form = UserForm(data=request.POST)
		
		# if not username:
			
			# return render(request, 'main.html', {'message': 'Please Sign Up First'})

		if user_form.is_valid():
			try:
				user = user_form.login()
			except Exception as e:
				message = 'Please Sign Up First'
			else:
				request.session['username'] = user.username;
			finally:
				username = request.session.get('username')
				return redirect('/?message=%s' % message)
			

# 			if user:				
# 				# del request.session['username']
# 				return render(request, 'main.html', {'users': username})
# #				return redirect('/index')

# 			else:
# 				return render(request, 'main.html', {'users': username})
# #				return redirect('/index')
		return redirect('/')

def file_upload(request):
	message= ""
	if request.method == 'GET':
		return redirect('/')

	else :
		username = request.session.get('username')
		if not username:
			message = "Please Login First"
			return redirect('/?message=%s' % message)

		picture_upload_form = PictureUploadForm(request.POST, request.FILES)
		if picture_upload_form.is_valid():

			poster = picture_upload_form.file_upload(username=username )

			print(poster)
			result = evnt_parser(detect_document(settings.BASE_DIR+poster.file.url))
			if poster:
				return render(request, 'main.html', {'result': result, 'posterId' : poster.id, 'poster' : poster, 'users': username })


		else:
			message = "Please Upload Poster"
			return redirect('/?message=%s' % message)

		# error handling
		return render(request, 'main.html', {'users': username })

def set_superuser(eventname, username):
	posters = Poster.objects.filter(eventname=eventname)
	for poster in posters:
		poster.eventholder = username
		print(poster.user.username)
		poster.save()


def feedback_upload(request):
	if request.method == 'GET':
		return redirect('/')

	else :
		print(request)
		feedback_form = FeedbackForm(request.POST, request.FILES)
		
		if feedback_form.is_valid():
			print(request.POST['posterid'])

			poster = feedback_form.feedback_upload(username=request.session['username'], posterId=request.POST['posterid'])
			if 'isholder' in request.POST:
				set_superuser(poster.eventname, request.session['username'])


			print(poster.file.url)
			#poster = feedback_form.feedback_upload(username=request.session['username'])
			data={}
			data['summary'] = poster.eventname
			data['location'] = ""
			data['description'] = poster.eventtext
			data['start'] = poster.eventdate
			data['end'] = poster.eventenddate
			#print(data)

			if poster:
				resultLink = create_event(data,request.session['username'])
			return render(request, 'main.html', {'posterId' : poster.id, 'poster' : poster, 'users': request.session['username'], 'resultLink' : resultLink})


		else:
			print(feedback_form.errors)


		return redirect('/')

def event_edit(request):
	if request.method == 'GET':
		return redirect('/')

	else :
		edit_form = EditForm(request.POST, request.FILES)
		if edit_form.is_valid():
			edit_form.edit_upload(eventname=request.POST['eventname'], new=request.POST['eventnewname'])
			print("DDDD")
			return redirect('/myimages')


		else:
			print(edit_form.errors)


	return redirect('/')

