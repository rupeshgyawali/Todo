from django import forms
from .models import Todo
from django.contrib.auth import models


class TodoForm(forms.Form):
	title = forms.CharField(label="Title")
	des = forms.CharField(label = "Description", widget=forms.Textarea)

class TodoModelForm(forms.ModelForm):
	class Meta:
		model = Todo
		fields = ['title', 'description']
		widgets = {
			'description': forms.Textarea(attrs={'rows': 5})
		}


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = models.User
		fields = ['username','email','password']

class LoginForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput)