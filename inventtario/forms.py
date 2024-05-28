from django import forms
from .models import Libro, Category

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'estado', 'tipo', 'imagen', 'cantidad_capitulos', 'cantidad_comentarios', 'cantidad_visualizaciones', 'categoria']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        
