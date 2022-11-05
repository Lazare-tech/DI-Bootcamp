from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def home(request):
    return render(request,'base.html')
def animals(request,id,*args, **kwargs):
    with open('templates/json/fichier.json','r') as fichier:
        my_json=fichier.read()
        context=json.loads(my_json)
        # taille=len(context[])
        # new= json.dumps(context, indent=2,sort_keys=True)
    return render(request,'animals.html',{'my_json':context['animals'][id]})    
def family(request,id_family,*args,**kargs):
    newContext=[]
    with open('templates/json/fichier.json','r') as fichier:
        my_json=fichier.read()
        context=json.loads(my_json)
        taille=len(context['animals'])
        name=[]
        for i in range(taille):

            if id_family==context['animals'][i]['id']:
                name=context['animals'][i]['name']
                # newContext.append(name)
        taille_famille=len(context['families'])  
        for i in range(taille_famille):
            if id_family==context['families'][i]['id']:
                
                name_famille=context['families'][i]['name']      
    return render(request,'family.html',{'name_famille':name_famille,'name':name})            
#EXERCISE XP GOLD,SUITE DE LEXERCICE XP CI-DESSUS        
#fonction qui liste tous les animaux
def animaux(request):
    with open('templates/json/fichier.json','r') as fichier:
        my_json=fichier.read()
        context=json.loads(my_json)
    taille=len(context)
    liste={}
    new=[]
    id=[]
    for i in range(taille+1):
            liste=(context['animals'])
    for j in liste:
        new.append(j['name'])  
        id.append(j['id']) 
    
        
    # newliste=context        
    return render(request,'animaux.html',{'liste':new,'id':id})   
     
