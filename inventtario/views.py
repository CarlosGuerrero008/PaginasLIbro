from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro
from .models import inventtario
from .models import Libro, Category
from django.shortcuts import render, redirect
from .forms import LibroForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def home(request):
    libros = Libro.objects.all()
    return render(request, 'index.html', {'libros': libros})

def anime_details(request):
    return render(request, 'anime-details.html')

def categories(request):
    libros = Libro.objects.all()
    return render(request, 'categories.html', {'libros': libros})

def vista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'lista_libros.html', {'libros': libros})

def index(request):
    libros = Libro.objects.all()
    return render(request, 'index.html', {'libros': libros})



def home(request):
    categorias = Category.objects.all().prefetch_related('libros')
    return render(request, 'index.html', {'categorias': categorias})

def categories(request):
    categorias = Category.objects.all()
    return render(request, 'categories.html', {'categorias': categorias})

def is_admin(user):
    return user.is_authenticated and user.is_staff

def admin_required(view_func):
    decorated_view_func = user_passes_test(is_admin, login_url='unauthorized')(view_func)
    return decorated_view_func

def unauthorized(request):
    return render(request, 'unauthorized.html')




from django.shortcuts import render, redirect
from .forms import LibroForm
from .models import Libro

@admin_required
def crear_libro(request):
    query = request.GET.get('q')  # Obtener el parámetro de búsqueda de la URL
    
    if query:  # Si hay una consulta de búsqueda
        libros = Libro.objects.filter(titulo__icontains=query)  # Filtrar libros por nombre que contenga la consulta
    else:
        libros = Libro.objects.all()  # Obtener todos los libros si no hay consulta
    
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LibroForm()
    
    return render(request, 'crear_libro.html', {'form': form, 'libros': libros, 'query': query})

from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Libro

def eliminar_libro(request, libro_id):  # Agregar libro_id como parámetro
    query = request.GET.get('q')  # Obtener el parámetro de búsqueda de la URL
    
    if query:  # Si hay una consulta de búsqueda
        libros = Libro.objects.filter(titulo__icontains=query)  # Filtrar libros por título que contenga la consulta
    else:
        libros = []  # Si no hay consulta, inicializar una lista vacía
    
    if request.method == 'POST':
        try:
            libro = Libro.objects.get(pk=libro_id)  # Obtener el libro utilizando el libro_id
            libro.delete()
            return redirect('home')
        except ObjectDoesNotExist:
            # Manejar el caso en que el libro no existe
            pass
    
    return render(request, 'home', {'libros': libros, 'query': query})

from django.shortcuts import render, redirect, get_object_or_404
from .forms import LibroForm
from .models import Libro

def editar_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)  # Obtener el libro a editar
    query = request.GET.get('q')  # Obtener el parámetro de búsqueda de la URL
    
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES, instance=libro)
        if form.is_valid():
            # Guardar el formulario sin hacer commit para no guardar todos los campos
            libro = form.save(commit=False)
            # Actualizar solo los campos que se hayan modificado
            for field in form.changed_data:
                setattr(libro, field, form.cleaned_data[field])
            # Guardar el libro con los campos actualizados
            libro.save()
            return redirect('home')
    else:
        form = LibroForm(instance=libro)  # Pasa la instancia del libro al formulario
    
    return render(request, 'editar_libro.html', {'form': form, 'libro': libro, 'query': query})


from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoryForm
from .models import Category
from django.views.decorators.http import require_POST

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_categoria')  # Redirigir a la misma página para ver la lista actualizada
    else:
        form = CategoryForm()
    
    categorias = Category.objects.all()
    
    return render(request, 'crear_categoria.html', {'form': form, 'categorias': categorias})

@require_POST
def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Category, pk=categoria_id)
    categoria.delete()
    return redirect('crear_categoria')  # Redirigir a la misma página para ver la lista actualizada

from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        # Creamos el usuario y lo guardamos en la base de datos
        user = User.objects.create_user(username=username, password=password, email=email)
        # Opcional: Puedes realizar alguna acción adicional, como enviar un correo de confirmación, por ejemplo.
        # Redirigimos a alguna página de éxito o cualquier otra página deseada.
        return redirect('home')  # Cambia 'success_page' al nombre de la URL a la que quieras redirigir después de agregar el usuario.
    else:
        return render(request, 'login.html')
    
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User

def user_signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redirige a la página deseada después de iniciar sesión
        else:
            error_message = 'Usuario o contraseña incorrectos'
            return render(request, 'signin.html', {'error_message': error_message})
    else:
        return render(request, 'signin.html')


    


    

    





    



