from django.contrib import admin
from ReceitaApp.models import Receita, Categoria
# Register your models here.

class Receitaadmin(admin.ModelAdmin):
    list_display = ['nome', 'grau_dificuldade']

class Categoriaadmin(admin.ModelAdmin):
    list_display = ['nome']

admin.site.register(Receita, Receitaadmin)
admin.site.register(Categoria)