# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from operator import itemgetter

contact_sample = ['010', '@']


def evnt_parser(contentList):
	#find the biggest one
	listSize = sorted(contentList, key=itemgetter('size'), reverse=True) 

	print("Supposed to Title : {}".format(listSize[0]["content"]))
	return({"title": listSize[0]["content"], "date": detect_date(listSize), "url": detect_url(listSize), "contact": detect_contact(listSize), "place": detect_place(listSize)})


def detect_date(contentList):
	sample = ['기간', '2017', '일시', '날짜']
	result = []
	for block in contentList:
		if any(element in block['content'] for element in sample):

			print("Supposed to Date : {}".format(block['content']))
			result.append(block['content'])
			'''matches = datefinder.find_dates(block['content'])
			for match in matches:
				print("Supposed to Date : {}".format(match))
				result.append(match)
			'''
	return result

def detect_url(contentList):
	sample = ['.com', '.kr', 'https://', 'com/']
	result = []
	for block in contentList:
		if any(element in block['content'] for element in sample) and not any(element in block['content'] for element in contact_sample):
			print("Supposed to url : {}".format(block['content']))
			result.append(block['content'])
	return result

def detect_contact(contentList):
	sample = ['010', '@']
	result = []
	for block in contentList:
		if any(element in block['content'] for element in sample):
			print("Supposed to contact : {}".format(block['content']))
			result.append(block['content'])
	return result


def detect_place(contentList):
	sample = ['장소', '위치']
	result = []
	for block in contentList:
		if any(element in block['content'] for element in sample):
			print("Supposed to place : {}".format(block['content']))
			result.append(block['content'])
	return result
