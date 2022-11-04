from django.shortcuts import render
from .models import Todo,Categorie

from .forms import TodoForm 
# Create your views here.

def home(request):
    return render(request,'base.html')
def todocreate(request):
    form= TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        form= TodoForm()
    
    return render(request,'todo_view.html',{'form':form}) 

def display_todos(request):
    todos=Todo.objects.all()
    context={
        'todos':todos
    }
    return render(request,'display_todos.html',context)