from django import forms
from .models import Todo,Categorie
import datetime

class TodoForm(forms.ModelForm):
    Categorie=forms.CharField(label='categorie')
    
    class Meta:
        model=Todo
        fields=['titre','details','has_been_done','date_creation','date_completion','date_echeance','categorie']
        # 'date_creation','date_completion','date_echeance']



