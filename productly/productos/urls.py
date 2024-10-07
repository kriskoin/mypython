#
# Course: ultimate python
# https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/
#
#
from django.urls import path
from  . import views
app_name = 'productos'
urlpatterns=[
    path('',views.index,name = 'index'),
    path('formulario',views.formulario,name='formulario'),
    path('<int:producto_id>',views.detalle,name = 'detalle'),
]