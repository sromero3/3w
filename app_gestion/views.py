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

    xClientes = Cliente.objects.values('id','ced_rif','nombre','telefono','ciudad__ciudad','status__statu').filter(status=1)
   
    context = {
        'xUsuario': xUsuario,
        'xClientes': xClientes
    }
    return render(request, 'app_gestion/clientes.html', context)

@login_required
def DocumentosView(request, xCliente, xVendedor,xIva):
    xUsuario = request.user

    xCliente_seleccionado  = 0
    xClientes = Cliente.objects.all()
    xIva_seleccionado  = 0
    xIvas = Iva.objects.all()
    xVendedor_seleccionado  = 0
    xVendedores = Vendedor.objects.all()

    if request.method == 'POST':
        # print("--------- Parametros recibidos POST ----------")
        xCliente_seleccionado  = int(request.POST.get('cliente'))
        xVendedor_seleccionado = int(request.POST.get('vendedor'))    
        xIva_seleccionado = int(request.POST.get('iva'))    
    
    qDocumentos = Documento.objects.values('id','numero','fecha','vencimiento','cliente__nombre','monto','iva__iva','cliente_id__ciudad__ciudad','cliente_id__vendedor__nombre', 'cliente_id__vendedor_id','observacion')
    #print(qDocumentos)

    if xCliente == 0 and xVendedor == 0 and xIva == 0:
       xDocumentos=qDocumentos
   

    elif xCliente == 0 and xVendedor == 0 and xIva != 0:
         xDocumentos=qDocumentos.filter(iva_id=xIva_seleccionado)

    elif xCliente == 0 and xVendedor != 0 and xIva != 0:
         xDocumentos=qDocumentos.filter(cliente_id__vendedor_id=xVendedor_seleccionado, iva_id=xIva_seleccionado)

    elif xCliente != 0 and xVendedor != 0 and xIva != 0:
         xDocumentos=qDocumentos.filter(cliente_id__vendedor_id=xVendedor_seleccionado, iva_id=xIva_seleccionado, cliente_id=xCliente_seleccionado)


    elif xCliente != 0 and xVendedor == 0 and xIva == 0:
         xDocumentos=qDocumentos.filter(cliente_id=xCliente_seleccionado)

    elif xCliente != 0 and xVendedor != 0 and xIva == 0:
         xDocumentos=qDocumentos.filter(cliente_id=xCliente_seleccionado, cliente_id__vendedor_id=xVendedor_seleccionado)
         

    elif xCliente != 0 and xVendedor == 0 and xIva != 0:
         xDocumentos=qDocumentos.filter(cliente_id=xCliente_seleccionado, iva_id=xIva_seleccionado)

    elif xCliente == 0 and xVendedor != 0 and xIva == 0:
         xDocumentos=qDocumentos.filter(cliente_id__vendedor_id=xVendedor_seleccionado)



    # elif xCliente == 0 and xVendedor != 0 and xIva != 0:
    #      xDocumentos=qDocumentos.filter(cliente_id__vendedor_id=xVendedor_seleccionado, iva_id=xIva_seleccionado)

    # elif xCliente != 0 and xVendedor != 0 and xIva != 0:
    #      xDocumentos=qDocumentos.filter(cliente_id__vendedor_id=xVendedor_seleccionado, iva_id=xIva_seleccionado, cliente_id=xCliente_seleccionado)


 
   
         


    
    context = {
        'xUsuario': xUsuario,
        'xDocumentos': xDocumentos,
        'xClientes': xClientes,
        'xCliente_seleccionado': xCliente_seleccionado,
        'xIvas': xIvas,
        'xIva_seleccionado': xIva_seleccionado,
        'xVendedores': xVendedores,
        'xVendedor_seleccionado': xVendedor_seleccionado,

         
    }
    return render(request, 'app_gestion/documentos.html', context)