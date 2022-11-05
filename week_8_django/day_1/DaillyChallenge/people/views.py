from ast import dump
from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]
def people_liste(request):
    
    my=[]
    name=[]
    for i in range(len(people[0])):
        # for data in people[i].items():
            name.append(people[i]["name"])
            # my.append(data[0]["name"])
    taille=len(name)
    id=taille-1
    return render(request,'home.html',{'my_json':name,'id':id})
def personne(request,id):
    my=[]
    for i in range(len(people[0])):
        for data in people[id].items():
            my.append(data)
            
        return render(request,'person.html',{'my_json':my})

       

