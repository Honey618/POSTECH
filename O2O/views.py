# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import UserForm, PictureUploadForm, FeedbackForm
from .parser.detect import *
from .parser.parser import *
#from .calendar.quickstart import *

def main(request):
	return render(request, 'main.html')

def myimages(request):
	from .models import Poster
	posters = Poster.objects.all()

	return render(request, 'myimages.html', {'posters': posters})

def index(request):
	from .models import Poster
	posters = Poster.objects.all()

	return render(request, 'main.html', {'posters': posters})

def sign_up(request):
	if request.method == 'GET':
		return redirect('/index')

	else:
		user_form = UserForm(data=request.POST)

		if user_form.is_valid():
			user = user_form.sign_up()

			if user:
				return redirect('/index')

			else:
				# TODO: 에러 처리 해줘야함
				return redirect('/index')
		return redirect('/index')

def login(request):
	if request.method == 'GET':
		return redirect('/index')

	else :
		user_form = UserForm(data=request.POST)

		if user_form.is_valid():
			user = user_form.login()

			if user:
				request.session['username'] = user.username
				
				print(request.session['username'])

				# del request.session['username']
				return render(request, 'main.html', {'user.username': user.username})
#				return redirect('/index')

			else:
				print(user.username)
				return render(request, 'main.html', {'user.username': user.username})
#				return redirect('/index')
		return redirect('/index')

def file_upload(request):
	if request.method == 'GET':
		return redirect('/index')

	else :
		picture_upload_form = PictureUploadForm(request.POST, request.FILES)
		if picture_upload_form.is_valid():
			poster = picture_upload_form.file_upload(username=request.session['username'])
			result = evnt_parser(detect_document(settings.BASE_DIR+poster.file.url))
			if poster:
				return render(request, 'main.html', {'result': result})

		else:
			print(picture_upload_form.errors)

		# error handling
		return redirect('/index')

def feedback_upload(request):
	if request.method == 'GET':
		return redirect('/index')

	else :
		print(request)
		feedback_form = FeedbackForm(request.POST, request.FILES)
		
		if feedback_form.is_valid():
			print(request.session['username'])

			poster = feedback_form.feedback_upload(username=request.session['username'])
			'''
			data={}
			data['summary']=poster.eventname
			data['location']="MY HOME"
			data['start']=poster.eventdate
			data['end']=poster.eventenddate
			data['description']=poster.eventtext
'''
			#create_event(data)
			if poster:
				return render(request, 'main.html')

		else:
			print(feedback_form.errors)



		return redirect('/index')

