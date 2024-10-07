# Para hacer los response
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
# For User Sign Up
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# from .forms import SignUpForm
from django.contrib import messages
from django.template.loader import get_template
from app_gestion.models import *

# Create your views here.
def Index_gestion(request):
    return render(request, 'app_gestion/index_app_gestion.html')

def InicioView(request):
    xAcceso = "Administrador"
    xUsuario = request.user
    
    return render(request, 'app_gestion/inicio.html')

@login_required
def ClientesView(request):
    xUsuario = request.user

    xClientes = Cliente.objects.values('id','ced_rif','nombre','telefono','ciudad__ciudad','status__status').filter(status=1)
    print(xClientes)
    context = {
        'xUsuario': xUsuario,
        'xClientes': xClientes
    }
    return render(request, 'app_gestion/clientes.html', context)