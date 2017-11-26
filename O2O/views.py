# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import UserForm, PictureUploadForm
	
def main(request):
	return render(request, 'main.html')

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

def login(request):
	if request.method == 'GET':
		return redirect('/index')

	else :
		user_form = UserForm(data=request.POST)

		if user_form.is_valid():
			user = user_form.login()

			if user:
				print('2')
				request.session['username'] = user.username
				
				print(request.session['username'])

				# del request.session['username']

				return redirect('/index')

			else:
				return redirect('/index')

def file_upload(request):
	if request.method == 'GET':
		return redirect('/index')

	else :
		picture_upload_form = PictureUploadForm(request.POST, request.FILES)
		if picture_upload_form.is_valid():
			poster = picture_upload_form.file_upload(username=request.session['username'])

			if poster:
				return redirect('/index')

		else:
			print(picture_upload_form.errors)

		# error handling
		return redirect('/index')