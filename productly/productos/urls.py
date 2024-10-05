#
# Course: ultimate python
# https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/
#
#
from django.urls import path
from  . import views

urlpatterns=[
    path('',views.index,name = 'index')
]