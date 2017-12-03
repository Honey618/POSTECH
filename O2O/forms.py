from django import forms
from .calendar import cal
class UserForm(forms.Form):
	username = forms.CharField()

	def sign_up(self):
		from .models import User

		if User.objects.filter(
			username=self.cleaned_data['username']
		).exists():
			raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
			return False

		user = User(
			username=self.cleaned_data['username'],
		)
		user.save()

		return user

	def login(self):
		from .models import User

		user_list = User.objects.filter(
			username=self.cleaned_data['username'],
		)

		if not user_list:
			raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
			return False

		else:
			return user_list[0]

class PictureUploadForm(forms.Form):
	file = forms.FileField()

	def file_upload(self, username):
		from .models import User, Poster

		poster = Poster.objects.create(
			user=User.objects.filter(username=username)[0],
			file=self.cleaned_data['file'],
		)
		return poster

class FeedbackForm(forms.Form):
	
	eventname = forms.CharField()
	eventdate = forms.CharField()
	eventenddate = forms.CharField(required=False)
	eventtext = forms.CharField(required=False)
	eventplace = forms.CharField(required=False)
	def feedback_upload(self, username, posterId):
		from .models import User, Poster

		poster = Poster.objects.get(id=posterId)

		poster.eventname=self.cleaned_data['eventname']
		poster.eventdate=self.cleaned_data['eventdate']
		if self.cleaned_data['eventenddate'] =='' :
			poster.eventenddate=self.cleaned_data['eventdate']
		else:
			poster.eventenddate=self.cleaned_data['eventenddate']

		poster.eventplace=self.cleaned_data['eventplace']
		poster.eventtext=self.cleaned_data['eventtext']
		poster.save()

		return poster

class EditForm(forms.Form):
	eventname = forms.CharField()
	eventnewname = forms.CharField()

	eventdate = forms.CharField()
	eventenddate = forms.CharField(required=False)
	eventtext = forms.CharField(required=False)
	eventplace = forms.CharField(required=False)
	def edit_upload(self, eventname, new):
		from .models import User, Poster
		print(eventname)
		posters = Poster.objects.filter(eventname=eventname)
		print(len(posters))
		for poster in posters:
			print(poster.eventname)
			print(self.cleaned_data['eventname'])
			poster.eventname=self.cleaned_data['eventnewname']
			poster.eventdate=self.cleaned_data['eventdate']
			if self.cleaned_data['eventenddate'] =='' :
				poster.eventenddate=self.cleaned_data['eventdate']
			else:
				poster.eventenddate=self.cleaned_data['eventenddate']

			poster.eventplace=self.cleaned_data['eventplace']
			poster.eventtext=self.cleaned_data['eventtext']
			poster.save()



