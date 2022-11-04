from django.db import models
from django.forms import ModelForm
# Create your models here.
# Create your models here.
class Categorie(models.Model):
    nom=models.CharField(max_length=30)
    image=models.ImageField()
    
    def __str__(self):
        return self.nom
    
#class todo model
class Todo(models.Model):
    titre=models.CharField(max_length=30)
    details=models.TextField()
    has_been_done=models.BooleanField(default=False)
    date_creation=models.DateTimeField()
    date_completion=models.DateTimeField()
    date_echeance=models.DateTimeField()
    categorie=models.ForeignKey(Categorie,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titre
    
