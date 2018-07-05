from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import TodoModelForm
from .models import Todo

# Create your views here.


def index(request):
	form = TodoModelForm(request.POST or None)
	if request.method == 'POST':
		# form = TodoModelForm(request.POST)
		if form.is_valid():
			# title = form.cleaned_data['title']
			# des = form.cleaned_data['description']
			form.save()
			return HttpResponseRedirect('/todo/')
	else:
		todo_list = Todo.objects.filter(is_completed__exact = False)
		completed_list = Todo.objects.filter(is_completed__exact = True)
		# form = TodoModelForm()
	return render(request, 'todo/index.html', {'form':form,
										'todo_list': todo_list,
										'completed_list': completed_list})


def delete(request, pk):
	obj = Todo.objects.get(pk=pk)
	obj.delete()
	return HttpResponseRedirect('/todo/')

def completed(request, pk):
	obj = Todo.objects.get(pk=pk)
	obj.is_completed = True
	obj.save()
	return HttpResponseRedirect('/todo/')