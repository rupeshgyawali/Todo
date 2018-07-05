from django import forms
from .models import Todo


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

