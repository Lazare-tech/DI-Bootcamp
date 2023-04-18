from django.shortcuts import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')