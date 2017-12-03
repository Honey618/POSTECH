# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from operator import itemgetter

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
        if(s[i]>='0' and s[i]<='9'):
            tmp1=s[i:]
            break;
    for i in range(len(tmp1)):
        I = len(tmp1)-1-i
        print(tmp1[I])
        if(tmp1[I]>='0' and tmp1[I]<='9'):
            tmp2=tmp1[:I+1]
            break;
    return tmp2

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

	return({"title": [listSize[0]["content"]], "date": dates, "url": url, "contact": contact, "place": place})

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
