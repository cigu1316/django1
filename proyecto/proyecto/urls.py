"""Configuración de URL del proyecto

La lista 'urlpatterns' enruta las URL a las vistas. Para obtener más información, consulte:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Ejemplos:
Vistas de funciones
    1. Agregar una importación: desde my_app vistas de importación
    2. Agregue una URL a urlpatterns: path('', views.home, name='home')
Vistas basadas en clases
  
Vistas basadas en clases
    1. Añadir una importación: desde other_app.views import Inicio
    2. Agregue una URL a urlpatterns: path('', Home.as_view(), name='home')
Incluir otra URLconf
    1. Importar la función include(): desde django.urls import include, path
    2. Agregue una URL a urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from proyecto.views import hola_mundo,otra_mas,fecha_actual,vista_con_edad,vista_con_template,saludo_desde_template,create_product 
from products.views import create_product,list_products,list_categorys,create_category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/',hola_mundo ),
    path('otra/',otra_mas),
    path('fecha/',fecha_actual),
    path('edad/<int:edad>/',vista_con_edad),
    path('vista-con-template/', vista_con_template),
    path('saludo-desde-template/',saludo_desde_template),
    
    path('create-product/',create_product),
    path('list-products/',list_products),
    
    path('create-category/<str:name>',create_category),
    path('list-categorys/',list_categorys)
    
]
