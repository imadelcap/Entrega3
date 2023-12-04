from django.urls import path
from AppTiendaBicicletas.views import formulario_accesorio, formulario_cliente, formulario_modelo_bicicleta, inicio, buscar_accesorio, buscar_cliente, buscar_modelo_bicicleta

urlpatterns = [
    path('crear_accesorio/', formulario_accesorio, name='crear accesorio'),
    path('crear_cliente/', formulario_cliente, name='crear cliente'),
    path('crear_modelo_de_bicicleta/', formulario_modelo_bicicleta, name='crear modelo de bicicleta'),
    path('inicio/', inicio, name='inicio'),
    path('buscar_accesorio/', buscar_accesorio, name='buscar accesorio'),
    path('buscar_cliente/', buscar_cliente, name='buscar cliente'),
    path('buscar_modelo_de_bicicleta/', buscar_modelo_bicicleta, name='buscar modelo de bicicleta')
]