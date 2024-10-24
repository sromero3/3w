from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from app_gestion.form import LoginForm

urlpatterns = [
     # Accesos
     path('', views.Index_gestion, name="index_gestion"), # Vista inicial del proyecto

     path('accounts/login/', auth_views.LoginView.as_view(
       authentication_form=LoginForm,
     ), name="login"),
    #        url     -    vista     -    nombre_u
     path('inicio/', views.InicioView, name='inicio'),
     path('clientes/', views.ClientesView, name='clientes'),
     path('documentos/<int:xCliente>/<int:xVendedor>/<int:xIva>/<int:xVencido>/', views.DocumentosView, name='documentos'),
     path('pagos/<int:id>/<cliente>/', views.Asentar_pagosView, name='pagos'),
     path('estado_cuentas/<int:id>/<cliente>/', views.Estado_cuentaView, name='estado_cuenta'),

     path('validar_referencia/', views.Validar_referenciaView, name='validar_referencia'),
     path('cargar_bancos/', views.Cargar_bancosView, name='cargar_bancos')
]