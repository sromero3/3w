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

     path('inicio/', views.InicioView, name='inicio'),
     path('clientes/', views.ClientesView, name='clientes'),
]