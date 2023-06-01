from django.urls import path
from .views import agregar_usuario, agregar_producto, buscar

urlpatterns = [
    path('agregar/usuario/', agregar_usuario, name='agregar_usuario'),
    path('agregar/producto/', agregar_producto, name='agregar_producto'),
    path('buscar/', buscar, name='buscar'),
]
