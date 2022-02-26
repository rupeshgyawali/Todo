from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from Todo.forms import LoginForm, UserForm
from django.contrib.auth import authenticate, login


def index(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/todo/')
	else:
		login_form = LoginForm()
		register_form = UserForm()
		
		if request.method == 'POST':

			if 'login_form' in request.POST:

				login_form = LoginForm(request.POST)

				if login_form.is_valid():
					username = request.POST['username']
					password = request.POST['password']
					user = authenticate(request,username=username,password=password)

					if user is not None:
						if user.is_active:
							login(request, user)
							return HttpResponseRedirect('/todo/')

			if 'register_form' in request.POST:

				register_form = UserForm(request.POST)

				if register_form.is_valid():
					user = register_form.save(commit=False)
					username = register_form.cleaned_data['username']
					password = register_form.cleaned_data['password']
					user.set_password(password)
					user.save()

					user = authenticate(request,username=username,password=password)

					if user is not None:
						if user.is_active:
							login(request, user)
							return HttpResponseRedirect('/todo/')


		return render(request, 'index.html',{'login_form':login_form, 'register_form':register_form})
