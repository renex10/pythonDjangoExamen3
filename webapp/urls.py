# webapp/urls.py
from django.urls import path
from . import views  # Importa las vistas desde el módulo actual (webapp)

urlpatterns = [
    path("", views.index, name="index"),  # URL para la página de inicio
    path("productos/", views.productos, name="productos"),  # URL para la página de productos
    path("categorias/", views.categorias, name="categorias"),  # URL para la página de categorías
    path("registrar/", views.registrar, name="registrar"),  # URL para la página de registro
    path("iniciar/", views.iniciar, name="iniciar"),  # URL para la página de iniciar sesión
    # Otros paths según tus necesidades
]

