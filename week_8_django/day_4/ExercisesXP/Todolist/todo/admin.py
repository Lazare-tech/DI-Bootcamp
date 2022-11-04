from django.contrib import admin
from .models import Categorie,Todo
# Register your models here.
class AdminCategorie(admin.ModelAdmin):
    list_display=('id','nom','image')
admin.site.register(Categorie,AdminCategorie)

class AdminTodo(admin.ModelAdmin):
    list_display=('id','titre','details','has_been_done','date_creation','date_completion','date_echeance','categorie')
admin.site.register(Todo,AdminTodo)    