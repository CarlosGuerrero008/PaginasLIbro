from django.contrib import admin
from .models import Libro, Category

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'estado', 'tipo', 'cantidad_capitulos', 'cantidad_comentarios', 'cantidad_visualizaciones')
    search_fields = ('titulo', 'estado', 'tipo')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)








