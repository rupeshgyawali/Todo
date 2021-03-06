from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from .forms import TodoModelForm, UserForm, LoginForm
from .models import Todo
from django.urls import reverse

# Create your views here.


def index(request):
	if request.method == 'POST':
		if 'listForm' in request.POST:
			form = TodoModelForm(request.POST or None)
			if form.is_valid():
				# title = form.cleaned_data['title']
				# des = form.cleaned_data['description']
				todo_item = form.save(commit=False)
				todo_item.user = request.user
				todo_item.save()
				return HttpResponseRedirect('/todo/')

		if 'registerForm' in request.POST:
			form = UserForm(request.POST)
			if form.is_valid():
				user = form.save(commit=False)
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				user.set_password(password)
				user.save()
				user = authenticate(request, username=username, password=password)
				
				if user is not None:
					if user.is_active:
						login(request, user)

				return HttpResponseRedirect('/todo/')

		if 'loginForm' in request.POST:
			form = LoginForm(request.POST)
			if form.is_valid():
				username = request.POST['username']
				password = request.POST['password']
				user = authenticate(request,username = username, password=password)

				if user is not None:
					if user.is_active:
						login(request,user)

	if request.user.is_authenticated:
		todo_list = request.user.todo_set.filter(is_completed__exact = False)
		completed_list = request.user.todo_set.filter(is_completed__exact = True)
	else:
		return HttpResponseRedirect('../')

	list_form = TodoModelForm()
	register_form = UserForm()
	login_form = LoginForm()


	return render(request, 'todo/index.html', {'list_form':list_form,
										'register_form': register_form,
										'login_form': login_form,
										'todo_list': todo_list,
										'completed_list': completed_list})

@login_required(login_url="/todo/")
def delete(request, pk):
	obj = Todo.objects.get(pk=pk)
	obj.delete()
	return HttpResponseRedirect('/todo/')

@login_required(login_url="/todo/")
def completed(request, pk):
	obj = Todo.objects.get(pk=pk)
	obj.is_completed = True
	obj.save()
	return HttpResponseRedirect('/todo/')

@login_required(login_url="/todo/")
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/todo/')
