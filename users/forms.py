from django import forms
from django.contrib.auth import get_user_model

User = get_user_model() 


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['email', 'phone_number', 'first_name', 'last_name']



class UserAvatarForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['avatar',]
			