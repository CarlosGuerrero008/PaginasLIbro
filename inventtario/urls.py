from django.urls import path
from . import views
from .views import add_user
from .views import login 
from .views import user_signin
from .views import unauthorized

urlpatterns = [
    path('', views.home, name='home'),  # Ruta para la vista de inicio
    path('add_user/', add_user, name='add_user'),
     path('login/', login, name='login'),  # Añadir la URL de login
    path('signin/', user_signin, name='signin'),
     path('unauthorized/', unauthorized, name='unauthorized'),
     
]

