from operator import itemgetter
import datefinder

contact_sample = ['010', '@']


def evnt_parser(contentList):
	#find the biggest one
	listSize = sorted(contentList, key=itemgetter('size'), reverse=True) 

	print("Supposed to Title : {}".format(listSize[0]["content"]))

	detect_date(listSize)
	detect_url(listSize)
	detect_contact(listSize)
	detect_place(listSize)

def detect_date(contentList):
	sample = ['기간', '2017', '일시', '날짜']
	for block in contentList:
		if any(element in block['content'] for element in sample):

			print("Supposed to Date : {}".format(block['content']))
			matches = datefinder.find_dates(block['content'])
			for match in matches:
				print("Supposed to Date : {}".format(match))

def detect_url(contentList):
	sample = ['.com', '.kr', 'https://', 'com/']
	for block in contentList:
		if any(element in block['content'] for element in sample) and not any(element in block['content'] for element in contact_sample):
			print("Supposed to url : {}".format(block['content']))

def detect_contact(contentList):
	sample = ['010', '@']
	for block in contentList:
		if any(element in block['content'] for element in sample):
			print("Supposed to contact : {}".format(block['content']))

def detect_place(contentList):
	sample = ['장소', '위치']
	for block in contentList:
		if any(element in block['content'] for element in sample):
			print("Supposed to place : {}".format(block['content']))