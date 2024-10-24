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
from django.db.models import Sum, Avg, Count
from django.db.models import F
from app_gestion.form import *
import csv
from app_gestion.functions import *
from decimal import Decimal
from django.http import JsonResponse


# Create your views here.
def Index_gestion(request):
    return render(request, 'app_gestion/index_app_gestion.html')

def InicioView(request):
    xAcceso = "Administrador"
    xUsuario = request.user

    # Actauliza los dias de vencimiento 
    hoy = date.today()
    xControl =  Control.objects.get(id=1)
    fecha_actual = datetime.now()
    if xControl.fecha_control != hoy:    
          # print("fechas dif voy a actaualzar")
          xDocumentos = Documento.objects.annotate(saldo = F('monto') - F('abonado')).filter(saldo__gt=0)
          for xDocumento in xDocumentos:
               fecha_str = xDocumento.vencimiento.strftime('%d/%m/%Y')
               # Convierte la cadena de texto a un objeto de fecha
               fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
                  # Resta la fecha dada de la fecha actual
               diferencia = fecha - fecha_actual
               xDocumento.dias_v = diferencia.days + 1 
               xDocumento.save()
    
               xControl.fecha_control = hoy
               xControl.save()
    #else
    #print("Ya esta actualizado")
  
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
def DocumentosView(request, xCliente, xVendedor, xIva, xVencido):
    xUsuario = request.user
    # print("--------- Parametros recibidos GET ----------")
    if xCliente != 0:
         xCliente_seleccionado = xCliente
    else:
        xCliente_seleccionado  = 0
    
    xClientes = Cliente.objects.all()
    xIva_seleccionado  = 0
    xIvas = Iva.objects.all()
    xVendedor_seleccionado  = 0
    xVendedores = Vendedor.objects.all()
    
    xVencido_seleccionado = 0

    if request.method == 'POST':
        # print("--------- Parametros recibidos POST ----------")
        xCliente_seleccionado  = int(request.POST.get('cliente'))
        xVendedor_seleccionado = int(request.POST.get('vendedor'))    
        xIva_seleccionado = int(request.POST.get('iva')) 
        if request.POST.get('vencido') == "on":
          #   xVencido = 1
            xVencido_seleccionado = 1
        else:
          #   xVencido = 0
            xVencido_seleccionado = 0
             
        
    if xVencido_seleccionado == 1:
       qDocumentos = Documento.objects.annotate(saldo = F('monto') - F('abonado')).filter(saldo__gt=0).values('id','numero','fecha','vencimiento','cliente__nombre','monto','iva__iva','cliente_id__ciudad__ciudad','cliente_id__vendedor__nombre', 'cliente_id__vendedor_id','observacion','abonado','saldo','dias_v').filter(dias_v__lte=0)
    else: 
       qDocumentos = Documento.objects.annotate(saldo = F('monto') - F('abonado')).filter(saldo__gt=0).values('id','numero','fecha','vencimiento','cliente__nombre','monto','iva__iva','cliente_id__ciudad__ciudad','cliente_id__vendedor__nombre', 'cliente_id__vendedor_id','observacion','abonado','saldo','dias_v')
 


    if xCliente == 0 and xVendedor == 0 and xIva == 0:
       xDocumentos=qDocumentos
     
    elif xCliente == 0 and xVendedor == 0 and xIva != 0:
         xDocumentos=qDocumentos.filter(iva_id=xIva_seleccionado)   

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

    elif xCliente == 0 and xVendedor != 0 and xIva != 0:
         xDocumentos=qDocumentos.filter(cliente_id__vendedor_id=xVendedor_seleccionado, iva_id=xIva_seleccionado)

    elif xCliente != 0 and xVendedor != 0 and xIva != 0:
         xDocumentos=qDocumentos.filter(cliente_id__vendedor_id=xVendedor_seleccionado, iva_id=xIva_seleccionado, cliente_id=xCliente_seleccionado)
 
    context = {
        'xUsuario': xUsuario,
        'xDocumentos': xDocumentos,
        'xClientes': xClientes,
        'xCliente_seleccionado': xCliente_seleccionado,
        'xIvas': xIvas,
        'xIva_seleccionado': xIva_seleccionado,
        'xVendedores': xVendedores,
        'xVendedor_seleccionado': xVendedor_seleccionado,
        'xVencido_seleccionado': xVencido_seleccionado,
    }
    
    return render(request, 'app_gestion/documentos.html', context)

@login_required
def Asentar_pagosView(request, id, cliente):
    xUsuario = request.user
    xCliente = cliente
    xId = id
 
    xFormas = PagoForma.objects.order_by('orden')
    xBancosdestino = BancoDestino.objects.exclude(id=6)
  
    xTasas = Tasa.objects.all()
    if xTasas.exists():
        xTasa = str(xTasas[0].monto)
    else:
        messages.error(
            request, "No ha fijado ninguna tasa de cambio")
        return redirect('inicio')

    form = asentar_pagoForm(request.POST)
    print(request.POST)
    if request.method == 'POST':
 
        # preparando los campos numericos
        request.POST._mutable = True
        if request.POST['monto'] == "":
            request.POST['monto'] = "0,00"

        if request.POST['banco_destino'] == "":
            request.POST['banco_destino'] = "6"
        print("---------------", request.POST['referencia'] )
        if request.POST['referencia'] == "":
            request.POST['referencia'] = "-"

        request.POST['monto'] = quitarFormato(request.POST['monto'])
        request.POST['tasa'] = quitarFormato(request.POST['tasa'])
        request.POST['monto_procesar'] = quitarFormato(request.POST['monto_procesar'])
   
        
        for field in form:
            print("Field:", field.name, "-> ", field.errors)
        
        if form.is_valid():

            pago = form.save(commit=False)
            pago.cliente_id = id
            pago.usuario_id = request.user.id
            form.save()
         

            # Actualizar el campo abono en los Documentos 
            xDocumentos = Documento.objects.annotate(saldo = F('monto') - F('abonado')).filter(saldo__gt=0).filter(cliente=id)
            xMonto_procesar = round(Decimal((request.POST['monto_procesar'])),2)
                  
            for xDocumento in xDocumentos:
                # El monto cubre el saldo del Doc
                if xMonto_procesar >= xDocumento.saldo:
                   xAbono = xDocumento.saldo
                   xDocumento.abonado = xDocumento.abonado + xAbono 
       
                else:
                # El monto no cubre el saldo del Doc
                   xAbono = xMonto_procesar  
                   xDocumento.abonado = xDocumento.abonado + xAbono
                   xAbono = xMonto_procesar  

                xDocumento.save()

                print("-------------Fac: " ,xDocumento.numero,"----------------")
                print("xMonto_procesar: " ,xMonto_procesar)
                print("Saldo: " ,xDocumento.saldo)
                xMonto_procesar = xMonto_procesar - xAbono
                print("xAbono: " ,xAbono)
                print("Monto restante",  xMonto_procesar )
               
                if xMonto_procesar == 0: 
                   print("no hay mas monto_procesar")
                   break
                
            if xMonto_procesar > 0:
                print("-------------Fac: " ,xDocumento.numero,"----------------")
                xAbono = xMonto_procesar  
                xDocumento.abonado = xDocumento.abonado + xAbono
                xDocumento.pago = pago.id
                xDocumento.save()
                print("xMonto_procesar: " ,xMonto_procesar)
                print("Saldo: " ,xDocumento.saldo)
                xMonto_procesar = xMonto_procesar - xAbono
                print("xAbono: " ,xAbono)
                print("Monto restante",  xMonto_procesar )
                print("--------- Sobro monto_procesar ----------")
            
            return redirect('documentos', id, 0, 0, 0)
        
        # redirect
     #    if xUsuario.profile.rango == "Usuario":  
     #        return redirect('inicio2')
        else:
           
           return redirect('inicio')

    
    context = {
        'xUsuario':xUsuario,
        'form': form,
        'xFormas': xFormas,
        'xTasa': xTasa,
        'xId': xId,
        'xCliente': xCliente,
        'xBancosdestino': xBancosdestino
    }
    return render(request, 'app_gestion/asentar_pago.html', context)

   
# validar si un proveedor ced_rif estste en un condominio
def Validar_referenciaView(request):
    # print('Dato: ',request.POST.get('campo'))
    data = {'status': False}
    Registro = Pago.objects.filter(referencia=request.POST.get('campo'))
    if Registro.exists():
        data = {'status': True}
    
    return JsonResponse(data, safe=False)

# cargar bancos destinos
def Cargar_bancosView(request):
    # print('Dato: ',request.POST.get('campo'))
    xBancosdestino = BancoDestino.objects.exclude(id=6).filter(tipo=request.POST.get('campo')).values('id','nombre')
    data = list(xBancosdestino)
    return JsonResponse(data, safe=False)

# estado de cuenta
@login_required
def Estado_cuentaView(request, id, cliente):
    xUsuario = request.user
    xCliente = cliente
    xId = id

    xClientes = Cliente.objects.all()
    
    if request.method == 'POST':
        print("clinte================",id)
        pass
    
    # obtengo los docuemntos
    qDocumentos = Documento.objects.filter(cliente=id).values('id','numero','fecha','monto')
    # obtengo los pagos
    qPagos = Pago.objects.filter(cliente=id).values('id','fecha','monto_procesar', 'forma__forma','referencia')

    xTotal = 0
    # Prepara lista de datos    
    balance = xTotal
    data_lista = []
    # data_lista.append({"fecha": fecha_i,"balance": xTotal})
    # data_lista.append({"balance": xTotal, "fecha": fecha_dt, "tipo__tipo": "Cierre", "concepto__concepto": "Saldo mes anterior "+xMes_nombre+" "+str(xAno) })
    for xAsiento in qDocumentos:
        xAsiento["documento"] = xAsiento['numero']
        xAsiento["forma"] = "-"
        xAsiento["dc"] = "+"
        xAsiento["monto_m"] = xAsiento['monto']
        balance += xAsiento['monto']
        xAsiento["balance"] = balance
        
        data_lista.append(xAsiento) # Se agrega cada registro a la lista
    
    for xAsiento in qPagos:
        xAsiento["documento"] = xAsiento['referencia']
        xAsiento["forma"] = xAsiento['forma__forma']
        xAsiento["dc"] = "-"
        xAsiento["monto_m"] = xAsiento['monto_procesar']
        balance += xAsiento['monto_procesar'] * -1
        xAsiento["balance"] = balance
        
        data_lista.append(xAsiento)
     
    context = {
        'xUsuario': xUsuario,
        'xCliente': xCliente,
        'xClientes': xClientes,
        'xId':xId,
        'xAsientos': data_lista
    }
    
    return render(request, 'app_gestion/estado_de_cuenta.html', context)


