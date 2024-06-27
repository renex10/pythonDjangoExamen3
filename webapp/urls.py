from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.registrar_productos, name='productos'),
    path('categorias/', views.registrar_categorias, name='categorias'),
    path('eliminar_categoria/<int:id>/', views.eliminar_categoria, name='eliminar_categoria'),
    path('editar_categoria/<int:id_categoria>/', views.editar_categoria, name='editar_categoria'),
    path('eliminar_producto/<int:id_producto>/', views.eliminar_producto, name='eliminar_producto'),
    path('editar_producto/<int:id_producto>/', views.editar_producto, name='editar_producto'),
    path('registrar/', views.registrar, name='registrar'),
    path('iniciar/', views.iniciar, name='iniciar'),
]

