# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from operator import itemgetter

from dateutil import parser
from datetime import datetime


contact_sample = ['문의']
place_sample = ['장소', '위치']
date_sample = ['기간', '일시', '날짜', '언제', 'when', '일정']
url_sample = ['https://', 'http://']

def include(element, lst):
    for l in lst:
        if (l in element.lower()):
            return True
    return False

def datecut(s):
    tmp1=""
    tmp2=""
    for i in range(len(s)):
        if(str(s[i])>='0' and str(s[i])<='9'):
            tmp1=s[i:]
            break;
    for i in range(len(tmp1)):
        I = len(tmp1)-1-i
        if(str(tmp1[I])>='0' and str(tmp1[I])<='9'):
            tmp2=tmp1[:I+1]
       
            if(tmp1[I+1:I+3].lower()=='am' or tmp1[I+1:I+3].lower()=='pm'):
            	tmp2=tmp1[:I+3]
            break;
    return tmp2

def parcut(s):
	flag1=False
	flag2=False
	start=0
	end=0
	for i in range(len(s)):
		if(s[i]=='('):
			flag1=True
			start=i
		elif(s[i]==')'):
			flag2=True
			end=i
	if (flag1 and flag2):
		return s[:start]+" "+s[end+1:]
	else:
		return s


def parse_list(contentList):
	content=[]
	for c in contentList:
		content.append(c['content'])
	for i in range(len(content)):

		for item in contact_sample:
			newcontent = content[i].replace(item, '*'+item).split('*')
			if newcontent[0] == '': newcontent.pop(0)
			if len(newcontent) is not 1:
				print(newcontent)
				content = content[:i]+newcontent+content[i+1:] 
		for item in place_sample:
			newcontent = content[i].replace(item, '*'+item).split('*')
			if newcontent[0] == '': newcontent.pop(0)
			if len(newcontent) is not 1:
				print(newcontent)
				content = content[:i]+newcontent+content[i+1:]

		for item in date_sample:
			newcontent = content[i].replace(item, '*'+item).split('*')
			if newcontent[0] == '': newcontent.pop(0)
			if len(newcontent) is not 1:
				print(newcontent)
				content = content[:i]+newcontent+content[i+1:]
		for item in url_sample:
			newcontent = content[i].replace(item, '*'+item).split('*')
			if newcontent[0] == '': newcontent.pop(0)
			if len(newcontent) is not 1:
				print(newcontent)

				content = content[:i]+newcontent+content[i+1:]
	return(content)

def evnt_parser(contentList):
	#find the biggest one
	listSize = sorted(contentList, key=itemgetter('size'), reverse=True) 

	print("Supposed to Title : {}".format(listSize[0]["content"]))
	newList = parse_list(listSize)

	date = detect_date(newList).pop(0)
	dates = datecut(date[0]).split('-')
	url = detect_url(newList)
	contact = detect_contact(newList)
	place = detect_place(newList)
	
	date[0]=datecut(date[0])
	a=parcut(date[0])
	print(a)
	a=a.replace("~",'-')
	a=a.replace(",",'.')
	a=a.replace("년",'.')
	a=a.replace("월",'.')
	a=a.replace("일",'.')
	b=a.split("-")
	result_data=[]
	if(len(b)==1):
		b[0]=parser.parse(b[0]).strftime('%Y-%m-%dT%H:%M:%S')
		result_data=[b[0],b[0],replace(hour=23, minute=59)]
	else:
		b[0]=parser.parse(b[0])
		b[1]=parser.parse(b[1])
		now = datetime.now()
		if(now.year==b[1].year and now.month==b[1].month and now.day==b[1].day):
			b[1]=b[1].replace(year=b[0].year, month=b[0].month, day=b[0].day)
		if(b[1].hour ==0 and b[1].minute == 0):
			b[1]=b[1].replace(hour=23, minute=59)
		result_data=[b[0].strftime('%Y-%m-%dT%H:%M:%S'), b[1].strftime('%Y-%m-%dT%H:%M:%S')]

	return({"title": [listSize[0]["content"]], "date": result_data, "url": url, "contact": contact, "place": place})


def detect_date(contentList):
    sample1 = ['기간', '일시', '날짜', '언제', 'when', '일정']
    sample5 = ['2017', '2018']
    sample2 = ['.','-','/','~']
    sample3 = ['mon', 'tue', 'wed', 'thu', 'thur', 'fri', 'sat', 'sun']
    sample4 = ['(월)','(화)','(수)','(목)','(금)','(토)','(일)']
    result = []
    for e in contentList:
        count=include(e, sample1)+include(e, sample2)+include(e, sample3)+include(e, sample4)+include(e, sample5)
        if(count>0):
            result.append([e,count])
    result= sorted(result, key=lambda tup: tup[1], reverse=True)
    return result

def detect_url(contentList):
	sample = ['.com', '.kr', 'https://', 'com/']
	result = []
	for e in contentList:
		if any(element in e for element in sample) and not any(element in e for element in contact_sample):
			print("Supposed to url : {}".format(e))
			result.append(e)
	return result

def detect_contact(contentList):
	sample = ['010', '@', '문의']
	result = []
	for block in contentList:
		if any(element in block for element in sample):
			print("Supposed to contact : {}".format(block))
			result.append(block)
	return result


def detect_place(contentList):
	prior_sample = ['장소', '위치']
	sample = ['호', '층', '실', '관']
	result = []
	for block in contentList:
		if any(element in block for element in prior_sample):
			print("Supposed to place : {}".format(block))
			result.append(block)
	if result==[]:
		for block in contentList:
			if any(element in block for element in sample):
				print("Supposed to place : {}".format(block))
				result.append(block)
	
	return result
