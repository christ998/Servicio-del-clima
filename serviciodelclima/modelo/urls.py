from django.urls import path
from modelo.views import home, form

urlpatterns = [
    path('',home),
    path('busqueda/', form),

]