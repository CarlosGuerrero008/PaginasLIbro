from django.contrib import admin
from django.urls import path
from inventtario import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Esta es la URL raíz
    path('anime-details.html/', views.anime_details, name='anime_details'),
    path('categories.html/', views.categories, name='categories'),
    path('crear_libro/', views.crear_libro, name='crear_libro'),
    path('login/', views.login, name='login'),  # Añadir la URL de login
    path('eliminar_libro/<int:libro_id>/', views.eliminar_libro, name='eliminar_libro'),
    path('editar_libro/<int:libro_id>/', views.editar_libro, name='editar_libro'),
    path('crear-categoria/', views.crear_categoria, name='crear_categoria'),
    path('eliminar-categoria/<int:categoria_id>/', views.eliminar_categoria, name='eliminar_categoria'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signin.html/', views.user_signin, name='signin.html'),
    path('unauthorized/', views.unauthorized, name='unauthorized'),
    
    
    
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
