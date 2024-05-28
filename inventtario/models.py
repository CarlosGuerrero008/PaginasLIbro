from django.db import models


# models.py
class inventtario(models.Model):
    # model fields go here
    name = models.CharField(max_length=100)
    # other fields


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Crear la categoría por defecto en una migración separada
def create_default_category(apps, schema_editor):
    Category = apps.get_model('your_app_name', 'Category')
    Category.objects.create(name='Sin categoría')

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='libros')
    cantidad_capitulos = models.IntegerField()
    cantidad_comentarios = models.IntegerField()
    cantidad_visualizaciones = models.IntegerField()
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='libros', default=1)

    def __str__(self):
        return self.titulo
    
