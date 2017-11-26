from django import forms


class UserForm(forms.Form):
	username = forms.CharField()

	def sign_up(self):
		from .models import User

		if User.objects.filter(
			username=self.cleaned_data['username']
		).exists():
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
			return False

		else:
			return user_list[0]

class PictureUploadForm(forms.Form):
	file = forms.FileField()

	def file_upload(self, username):
		from .models import User, Poster

		poster = Poster.objects.create(
			participant=User.objects.filter(username=username)[0],
			file=self.cleaned_data['file'],
		)

		return poster

		