# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from operator import itemgetter

contact_sample = ['010', '@']

def include(element, lst):
    for l in lst:
        if (l in element.lower()):
            return True
    return False


def evnt_parser(contentList):
	#find the biggest one
	listSize = sorted(contentList, key=itemgetter('size'), reverse=True) 

	print("Supposed to Title : {}".format(listSize[0]["content"]))

	return({"title": [listSize[0]["content"]], "date": detect_date(listSize), "url": detect_url(listSize), "contact": detect_contact(listSize), "place": detect_place(listSize)})

def detect_date(contentList):
    sample1 = ['기간', '일시', '날짜', '언제', 'when', '일정']
    sample5 = ['2017', '2018']
    sample2 = ['.','-','/','~']
    sample3 = ['mon', 'tue', 'wed', 'thu', 'thur', 'fri', 'sat', 'sun']
    sample4 = ['(월)','(화)','(수)','(목)','(금)','(토)','(일)']
    result = []
    for block in contentList:
        e= block['content']
        count=include(e, sample1)+include(e, sample2)+include(e, sample3)+include(e, sample4)+include(e, sample5)
        if(count>0):
            result.append([e,count])
    result= sorted(result, key=lambda tup: tup[1], reverse=True)
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
