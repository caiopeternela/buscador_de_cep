from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('endereco/', views.endereco),
    path('api/<cep>', views.api)
]