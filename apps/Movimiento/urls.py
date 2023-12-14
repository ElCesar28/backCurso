# Importaciones necesarias de Django
from django.urls import path
from apps.Movimiento.api import movimiento_api_view

urlpatterns = [
    path('movimientos/', movimiento_api_view, name='movimiento_api_view'),
]
