from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from registration.models import UserProfile
from django.contrib.auth import hashers


class RegistrationForm(ModelForm):
	username = forms.CharField(label=(u'User Name'))
	email = forms.EmailField(label=(u'Email Address'))
	password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
	password1 = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))

	class Meta:
		model = UserProfile
		exclude = ('user',)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError("That username is already taken, please select another.")

	def clean_contact(self):
		contact = self.cleaned_data['contact']
		try:
			UserProfile.objects.get(contact=contact)
		except UserProfile.DoesNotExist:
			return contact
		raise forms.ValidationError("This Mobile Number is already registered.")

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError("This Email-id is already registered.")

	def clean(self):
		password = self.cleaned_data['password']
		password1 = self.cleaned_data['password1']
		if password != password1:
			raise forms.ValidationError("The passwords did not match. Please try again.")
		return self.cleaned_data

class LoginForm(forms.Form):
	username = forms.CharField(label=(u'User Name'))
	password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))

	def clean(self):
		username = self.cleaned_data['username']
		password = self.cleaned_data['password']
		try:
			myuser =  User.objects.get(username=username)
			if hashers.check_password(password, myuser.password):
				return self.cleaned_data	
			else:
				raise forms.ValidationError("Wrong username or password")
				
				
		except:
			raise forms.ValidationError("Wrong username or password")

			
		