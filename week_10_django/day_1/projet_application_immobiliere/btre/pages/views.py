from django.shortcuts import HttpResponse
from django.shortcuts import render,redirect
from realtors.models import Realtor
from listings.models import Listing
# Create your views here.
def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
 
    context={
        'listings':listings
    }
    return render(request,'home.html',context)

def about(request):
    #realtors
    realtors= Realtor.objects.order_by('-hire_date')
    #mvp
    mvp_realtors= Realtor.objects.all().filter(is_mvp=True)
    context={
        'realtors':realtors,
        'mvp_realtors':mvp_realtors,
    }
    return render(request,'about.html',context)