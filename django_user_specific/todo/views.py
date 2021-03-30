from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Todo, Item
from .forms import TodoForm, CreateNewList
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponse

@login_required
def home(response, id):
	todo_list = Todo.objects.get(id=id)
	items = todo_list.item_set.all(id=1)
	context={"todo_list":todo_list.name}
	return HttpResponse("<h1>%s</h1><br></br><p>%s</P>"%(todo_list.name, str(items.text)))

@require_POST
def addTodo(request):
	form = TodoForm(request.POST)
	if form.is_valid():
		new_todo = Todo(text=request.POST['text'])
		new_todo.save()
	return redirect('todo-home')

#-------------------------------------MAKE ITEM ON TODO COMPLETE------------------------------#

def completeTodo(request, todo_id):
	todo = Todo.objects.get(pk=todo_id)
	todo.complete = True
	todo.save()
	return redirect('todo-home')

#-------------------------------------DELETE COMPLETED TODO ITEMS------------------------------#

def deleteCompleted(request):
	Todo.objects.filter(complete__exact=True).delete()
	return redirect('todo-home')

#-------------------------------------DELETE ALL TODO ITEMS------------------------------#

def deleteAll(request):
	Todo.objects.all().delete()

	return redirect('todo-home')

def create(response):
	if response.method == "POST":
		form = CreateNewList(response.POST)
		if form.is_valid():
			n = form.cleaned_data["name"]
			t = Todo(name=n)
			t.save()
		return HttpResponseRedirect("/%i"%t.id)
	else:
		form = CreateNewList()
	return render(response, "todo/create.html", {"form":form})