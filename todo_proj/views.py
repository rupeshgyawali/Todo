from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from Todo.forms import LoginForm, UserForm
from django.contrib.auth import authenticate, login


def index(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/todo/')
	else:
		if request.method == 'POST':

			if 'login_form' in request.POST:

				form = LoginForm(request.POST)

				if form.is_valid:
					username = request.POST['username']
					password = request.POST['password']
					user = authenticate(request,username=username,password=password)

					if user is not None:
						if user.is_active:
							login(request, user)
							return HttpResponseRedirect('/todo/')

			if 'register_form' in request.POST:

				form = UserForm(request.POST)

				if form.is_valid:
					user = form.save(commit=False)
					username = form.cleaned_data['username']
					password = form.cleaned_data['password']
					user.set_password(password)
					user.save()

					user = authenticate(request,username=username,password=password)

					if user is not None:
						if user.is_active:
							login(request, user)
							return HttpResponseRedirect('/todo/')


		login_form = LoginForm()
		register_form = UserForm()
		return render(request, 'index.html',{'login_form':login_form, 'register_form':register_form})
