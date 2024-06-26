from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("productos/", views.registrar_productos, name="productos"),
    path("categorias/", views.registrar_categorias, name="categorias"),
    path("registrar/", views.registrar, name="registrar"),
    path("iniciar/", views.iniciar, name="iniciar"),
    path('eliminar_categoria/<int:id_categoria>/', views.eliminar_categoria, name='eliminar_categoria'),
]


