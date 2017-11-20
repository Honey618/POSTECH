# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

def main(request):
	return render(request, 'main.html')
	
def index(request):
	msg = "Hello, world. You're at the polls index."
	return render(request, 'index.html', {'message': msg})