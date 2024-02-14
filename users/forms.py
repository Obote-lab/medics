from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Profile


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(max_length=100, help_text='<strong color: "green">Required.Add a valid email Address</strong>')

	class Meta:
		model = User
		fields = ['username', 'email','password1', 'password2'] 


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField(max_length=100, help_text='<strong color: "green">Required.Add a valid email Address</strong>')

	class Meta:
		model = User
		fields = ['username', 'email',] 


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']
