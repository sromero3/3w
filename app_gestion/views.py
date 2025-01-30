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
from operator import itemgetter
from datetime import datetime, timedelta
from django.db.models import Q
from decimal import *
import os
from django.contrib.auth import logout

# from weasyprint import HTML


# Create your views here.
def Index_gestion(request):
    return render(request, 'app_gestion/index_app_gestion.html')

def InicioView(request):
    xAcceso = "Administrador"
    xUsuario = request.user

    # Actauliza los dias de vencimiento 
    actualizar_dias_vencido()
    
    # calcualar tolal 
    qDocumentos = Documento.objects.annotate(saldo = F('monto') - F('abonado')).filter(saldo__gt=0)
    qTotal = qDocumentos.aggregate(total=Sum("saldo")).get('total')
    total_cxc = qTotal

    # Busca la tasa catual
    xTasas = Tasa.objects.all()
    if xTasas.exists():
        xTasa = xTasas[0].monto
        xActual = xTasas[0].actualizado
    else:
        messages.error(
            request, "No ha fijado ninguna tasa de cambio")
        return redirect('tasas')
    
    context = {
      'total_cxc': total_cxc,
      'xTasa': xTasa,
      'xActual': xActual
    }
    
    return render(request, 'app_gestion/inicio.html', context)


@login_required
def ClientesView(request, xStatus, xVendedor):
    xUsuario = request.user
    # print("--------- Parametros recibidos GET ----------")
  
    xStatu_seleccionado = xStatus
    xVendedor_seleccionado = xVendedor
    xExcluidos = [2, 4]
    xStatus_select = Statu.objects.exclude(id__in=xExcluidos)
    xVendedores = Vendedor.objects.filter(status_id=1).order_by('nombre')

    if request.method == 'POST':
        # print("--------- Parametros recibidos POST ----------")
        xStatu_seleccionado  = request.POST.get('f_status')
        xVendedor_seleccionado = request.POST.get('f_vendedor')

    qClientes = Cliente.objects.values('id','ced_rif','nombre','vendedor__nombre','status__statu').order_by("nombre")

    if xStatus == 0  and xVendedor == 0:
        xClientes=qClientes
    elif xStatus != 0 and xVendedor != 0:
        xClientes=qClientes.filter(status_id=xStatus, vendedor_id = xVendedor)
    elif xStatus != 0 and xVendedor == 0:
        xClientes=qClientes.filter(status_id=xStatus)
    elif xStatus == 0 and xVendedor != 0:
        xClientes=qClientes.filter(vendedor_id = xVendedor)

   
    context = {
        'xUsuario': xUsuario,
        'xClientes': xClientes,
        'xStatus_select':xStatus_select,
        'xStatu_seleccionado': int(xStatu_seleccionado),
        'xVendedor_seleccionado': int(xVendedor_seleccionado),
        'xVendedores': xVendedores 

    }
    return render(request, 'app_gestion/clientes.html', context)


@login_required
def add_clienteView(request):
    # xUsuario = request.user
    xOpcion = "Agregando"
      
    xPrefijos_ced_rif = Prefijo_ced_rif.objects.all()
    xVendedores = Vendedor.objects.filter(status_id=1).order_by('nombre')
    xCiudades = Ciudad.objects.all()
       
    form = agregar_clienteForm()

    if request.method == 'POST':
        form = agregar_clienteForm(request.POST)

        request.POST._mutable = True
        request.POST['status'] = 1
        request.POST['ced_rif'] =  request.POST['prefijo_r'] + request.POST['ced_rif'] 
       
        # for field in form:
        #       print("Field:", field.name, "-> ", field.errors)
    
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.usuario_id = request.user.id

            cliente.save()

            # Limpiara formulario para otro gasto
            form = agregar_clienteForm()
            context = {
               'form': form,
               'xOpcion': xOpcion,
               'xPrefijos_ced_rif':xPrefijos_ced_rif,
               'xVendedores': xVendedores,
               'xCiudades': xCiudades,
               'rNum_cedula': "",
               'otro': True,
            }

            return render(request, 'app_gestion/clientes_crud.html', context)
        else:
            messages.error(
                request, "Su operación no se puedo efectuar debido a problemas en el Servidor. El formulario no es válido")
    
    context = {
      'form': form,
      'xOpcion': xOpcion,
      'xPrefijos_ced_rif':xPrefijos_ced_rif,
      'xVendedores': xVendedores,
      'xCiudades': xCiudades,
      'rNum_cedula': "",
      'otro': False  
    }
    return render(request, 'app_gestion/clientes_crud.html', context)


@login_required
def Editar_clienteView(request, id):
    xUsuario = request.user
    xOpcion = "Editando"
   
    xPrefijos_ced_rif = Prefijo_ced_rif.objects.all()
    xPrefijos = Prefijo_telefono.objects.all()
    xCiudades = Ciudad.objects.all()
    xVendedores = Vendedor.objects.filter(status_id=1).order_by('nombre')
    xStatus = Statu.objects.all()
    
    # Obtengo el registro a editar
    xCliente = Cliente.objects.get(id=id)
    rPrer_Ced_rif = xCliente.ced_rif[0:1]
    rCed_rif = xCliente.ced_rif[1:]
    rVendedor = xCliente.vendedor.id
    rStatu = xCliente.status.id
    rNum_cedula = xCliente.ced_rif
  
    form = agregar_clienteForm(instance=xCliente)

    if request.method == 'POST':
        form = agregar_clienteForm(request.POST, instance=xCliente)
        # request.POST._mutable = True
    
        # for field in form:
        #      print("Field:", field.name, "-> ", field.errors)
        
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.ced_rif = request.POST.get('prefijo_r') + request.POST.get('ced_rif')
            cliente.save()
            return redirect('clientes',1, 0)
        else:
            messages.error(
                request, "Su operación no se puedo efectuar debido a problemas en el Servidor. El formulario no es válido")

    context = {
        'form': form,
        'xOpcion': xOpcion,
        'xPrefijos_ced_rif': xPrefijos_ced_rif,
        'rPrer_Ced_rif': rPrer_Ced_rif,
        'rCed_rif': rCed_rif,
        'xPrefijos': xPrefijos,
        'xCiudades': xCiudades,
        'xVendedores': xVendedores,
        'rVendedor': rVendedor,
        'xStatus': xStatus,
        'rStatu': rStatu,
        'rNum_cedula': rNum_cedula
    }
    return render(request, 'app_gestion/clientes_crud.html', context)


@login_required
def documentosView(request, xCliente, xDias):
    xUsuario = request.user
    # print("--------- Parametros recibidos GET ----------")
    if xCliente != 0:
        xCliente_seleccionado = xCliente
    else:
        xCliente_seleccionado  = 0

    xDia_seleccionado = xDias
    dias_a_restar = 45
    hoy = date.today()
    
    xClientes_select = Cliente.objects.all()
    xDias_select = Dia.objects.all()
    
    
    if request.method == 'POST':
        # print("--------- Parametros recibidos POST ----------")
        xCliente_seleccionado  = request.POST.get('cliente')
        xDia_seleccionado  = request.POST.get('dias')

    actualizar_dias_vencido()
    qDocumentos = Documento.objects.annotate(saldo = F('monto') - F('abonado')).values('saldo','id','numero','fecha','vencimiento','cliente__nombre','monto','iva__iva','condicion__condicion','cliente_id__vendedor__nombre', 'cliente_id__vendedor_id','observacion','abonado', 'dias_v','credito').order_by('-id')

   
    if xCliente == 0 and xDias == 0:
        #  print("1 sin filtros")
         xDocumentos=qDocumentos

    elif xCliente == 0 and xDias != 0: 
         fecha_atras = hoy - timedelta(days=dias_a_restar)
        #  print("2 por defecto = todos los clientes con dias atras",dias_a_restar, fecha_atras )
         xDocumentos=qDocumentos.filter(fecha__gt=fecha_atras)
    
    elif xCliente != 0 and xDias == 0: 
        #  print("3 mostar este clinte con todas",xDia_seleccionado )
         xDocumentos=qDocumentos.filter(cliente_id=xCliente)
    elif xCliente != 0 and xDias != 0: 
         fecha_atras = hoy - timedelta(days=dias_a_restar)
        #  print(" 4 mostar este clinte con dias atras",dias_a_restar, fecha_atras )
         xDocumentos=qDocumentos.filter(cliente_id=xCliente, fecha__gt=fecha_atras)
         
    context = {
        'xUsuario': xUsuario,
        'xDocumentos': xDocumentos,
        'xClientes_select':  xClientes_select,
        'xCliente_seleccionado': int(xCliente_seleccionado),
        'xDia_seleccionado': int(xDia_seleccionado),
        'xDias_select': xDias_select
    }
   
    return render(request, 'app_gestion/documentos.html', context)


@login_required
def add_documentoView(request):
    # xUsuario = request.user
    xOpcion = "Agregando"
       
    xClientes = Cliente.objects.filter(status_id=1)
    xIvas = Iva.objects.all()
    xCondiciones = Condicion.objects.all()
    xCredito = Credito.objects.all()

    # para agregar cleinte desde documento
    xPrefijos_ced_rif = Prefijo_ced_rif.objects.all()
    xVendedores = Vendedor.objects.filter(status_id=1).order_by('nombre')
       
    form = agregar_documentoForm()

    if request.method == 'POST':
        form = agregar_documentoForm(request.POST)

        request.POST._mutable = True
        request.POST['monto'] = quitarFormato(request.POST['monto'])
        request.POST['vencimiento'] = datetime.strptime(request.POST['vencimiento'], '%Y-%m-%d')
       
        # for field in form:
        #      print("Field:", field.name, "-> ", field.errors)

        hoy = datetime.now()

        if form.is_valid():
            fecha_actual = datetime.now()
            documento = form.save(commit=False)
            documento.usuario_id = request.user.id
            diferencia = request.POST['vencimiento'] - fecha_actual
            documento.dias_v = diferencia.days + 1
            documento.credito = request.POST['credito']
            documento.actualizado = hoy
            documento.save()

            # Buscar en excedentes
            xExcedente = Excedente.objects.filter(cli_id=request.POST.get('cliente'), saldo__gt=0).values('doc_id__numero','saldo')
            if xExcedente.exists(): # si el cliente tiene Excedente
                xNumero = xExcedente[0]['doc_id__numero']
                if xExcedente[0]['saldo'] > Decimal(request.POST.get('monto')):
                    xE = request.POST.get('monto')
                    xS = xExcedente[0]['saldo']
                else:
                    xE = xExcedente[0]['saldo']
                    xS = xExcedente[0]['saldo']
                # guardar pago
                pago = Pago(fecha = request.POST.get('fecha'), cliente_id = request.POST.get('cliente'), referencia = "Abono excedente Doc: "+xNumero,
                            monto = 0, monto_procesar = Decimal(xE), forma_id = 5, tasa = 0, banco_destino_id = 6, usuario_id = request.user.id,
                            actualizado = hoy)
                pago.save() 
                xPago_id = pago.id     
                # guardar detelle del pago
                detalle = Pago_detalle(pago_id = xPago_id, documento_id =  documento.id, monto_procesar = xE)  
                detalle.save()
                # actualizo abonado en Documento
                documento.abonado = xE
                documento.save()
                # actualizo el saldo en excedente
                xS = xS - Decimal(xE)
                xExcedente.update(saldo=xS)

            # Limpiara formulario para otro gasto
            form = agregar_documentoForm()
            context = {
               'form': form,
               'xOpcion': xOpcion,
               'xClientes': xClientes,
               'xCreditos': xCredito,
               'xIvas': xIvas,
               'rNum': "",
               'xCondiciones': xCondiciones,
               'xPrefijos_ced_rif': xPrefijos_ced_rif,
               'xVendedores': xVendedores,
               'otro': True
            }

            return render(request, 'app_gestion/documentos_crud.html', context)
        else:
            messages.error(
                request, "Su operación no se puedo efectuar debido a problemas en el Servidor. El formulario no es válido")
    
    context = {
     'form': form,
     'xOpcion': xOpcion,
     'xClientes': xClientes,
     'xCreditos': xCredito,
     'xIvas': xIvas,
     'xCondiciones': xCondiciones,
     'rNum': "",
     'xPrefijos_ced_rif': xPrefijos_ced_rif,
     'xVendedores': xVendedores,
     'otro': False  
    }
    return render(request, 'app_gestion/documentos_crud.html', context)


@login_required
def Editar_documentoView(request, id):
    xUsuario = request.user
    xOpcion = "Editando"
   
    xClientes = Cliente.objects.filter(status_id=1)
    xIvas =  Iva.objects.all()
    xCondiciones = Condicion.objects.all()
    
    # Obtengo el registro a editar
    xDocumento = Documento.objects.get(id=id)
    rClienteId = xDocumento.cliente.id
    rIvaId = xDocumento.iva.id
    rCondicionId = xDocumento.condicion.id
    rNum = xDocumento.numero
  
   
    form = agregar_documentoForm(instance=xDocumento)

    if request.method == 'POST':
        form = agregar_documentoForm(request.POST, instance=xDocumento)

        request.POST._mutable = True
        # print(request.POST['monto'])
        request.POST['monto'] = quitarFormato(request.POST['monto'])
        # print(request.POST['monto'])
        request.POST['vencimiento'] = datetime.strptime(request.POST['vencimiento'], '%Y-%m-%d')
        request.POST['fecha'] = datetime.strptime(request.POST['fecha'], '%Y-%m-%d')
        for field in form:
             print("Field:", field.name, "-> ", field.errors)
        
        if form.is_valid():
            fecha_actual = datetime.now()
            documento = form.save(commit=False)
            diferencia = request.POST['vencimiento'] - fecha_actual 
            documento.dias_v = diferencia.days + 1
            dias_credito =  request.POST['vencimiento'] - request.POST['fecha']
            documento.credito = dias_credito.days

            documento.save()
            return redirect('documentos',0, 1)
        else:
            messages.error(
                request, "Su operación no se puedo efectuar debido a problemas en el Servidor. El formulario no es válido")

    context = {
        'form': form,
        'xOpcion': xOpcion,
        'xClientes': xClientes,
        'rClienteId': rClienteId,
        'xIvas': xIvas,
        'xCondiciones': xCondiciones,
        'rIvaId': rIvaId,
        'rCondicionId':rCondicionId,
        'rNum': rNum,
    }

    return render(request, 'app_gestion/documentos_crud.html', context)


@login_required
def cobranzaView(request, xCliente, xVendedor, xIva, xVencido):
    xUsuario = request.user
    # print("--------- Parametros recibidos GET ----------")

    if xCliente != 0:
        xCliente_seleccionado = xCliente
    else:
        xCliente_seleccionado  = 0

    if xVendedor != 0:
        xVendedor_seleccionado = xVendedor
        print("Mostrar clientes del vel vendor ", xVendedor_seleccionado)
        xClientes = Cliente.objects.filter(Q( status_id=1) | Q(status_id=2)).filter(vendedor_id=xVendedor)
    else:
        xVendedor_seleccionado  = 0
        xClientes = Cliente.objects.filter(Q( status_id=1) | Q(status_id=2))

    
    # xClientes = Cliente.objects.filter(Q( status_id=1) | Q(status_id=2))
    xIva_seleccionado  = 0
    xIvas = Iva.objects.all()
    xVendedor_seleccionado  = 0
    xVendedores = Vendedor.objects.filter(status_id=1).order_by('nombre')
    
    xVencido_seleccionado = 0

    if request.method == 'POST':
        # print("--------- Parametros recibidos POST ----------")
        xCliente_seleccionado  = request.POST.get('cliente')
        xVendedor_seleccionado = request.POST.get('vendedor')
        xIva_seleccionado = request.POST.get('iva') 
        if request.POST.get('vencido') == "on":
          #   xVencido = 1
            xVencido_seleccionado = 1
        else:
          #   xVencido = 0
            xVencido_seleccionado = 0


    actualizar_dias_vencido()
    if xVencido_seleccionado == 1:
       qDocumentos = Documento.objects.annotate(saldo = F('monto') - F('abonado')).filter(saldo__gt=0).values('id','numero','fecha','vencimiento','cliente__nombre','monto','iva__iva','cliente_id__vendedor__nombre', 'cliente_id__vendedor_id','observacion','abonado','saldo','dias_v','condicion__condicion','credito').filter(dias_v__lte=0)
    else: 
       qDocumentos = Documento.objects.annotate(saldo = F('monto') - F('abonado')).filter(saldo__gt=0).values('id','numero','fecha','vencimiento','cliente__nombre','monto','iva__iva','cliente_id__vendedor__nombre', 'cliente_id__vendedor_id','observacion','abonado','saldo','dias_v','condicion__condicion','credito')
 
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
    
    xDoc_encontrados = xDocumentos.count()
 
    context = {
        'xUsuario': xUsuario,
        'xDocumentos': xDocumentos,
        'xClientes': xClientes,
        'xCliente_seleccionado': int(xCliente_seleccionado),
        'xIvas': xIvas,
        'xIva_seleccionado': int(xIva_seleccionado),
        'xVendedores': xVendedores,
        'xVendedor_seleccionado': int(xVendedor_seleccionado),
        'xVencido_seleccionado': xVencido_seleccionado,
        'xDoc_encontrados': xDoc_encontrados 
    }
    
    return render(request, 'app_gestion/cobranza.html', context)


@login_required
def Pago_cuentaView(request, id, cliente):
    xUsuario = request.user
    xCliente = cliente
    xId = id
 
    xFormas = PagoForma.objects.order_by('orden').exclude(id=5)
    xBancosdestino = BancoDestino.objects.exclude(id=6)
  
    xTasas = Tasa.objects.all()
    if xTasas.exists():
        xTasa = str(xTasas[0].monto)
    else:
        messages.error(
            request, "No ha fijado ninguna tasa de cambio")
        return redirect('inicio')
    
    hoy = datetime.now()

    form = asentar_pagoForm(request.POST)
    if request.method == 'POST':
 
        # preparando los campos numericos
        request.POST._mutable = True
        if request.POST['monto'] == "":
            request.POST['monto'] = "0,00"

        if request.POST['banco_destino'] == "":
            request.POST['banco_destino'] = "6"
      
        if request.POST['referencia'] == "":
            request.POST['referencia'] = "-"

        request.POST['monto'] = quitarFormato(request.POST['monto'])
        request.POST['tasa'] = quitarFormato(request.POST['tasa'])
        request.POST['monto_procesar'] = quitarFormato(request.POST['monto_procesar'])
        strMonto_procesar = darFormato(request.POST['monto_procesar'])
       
        if form.is_valid():
            pago = form.save(commit=False)
            pago.cliente_id = id
            pago.usuario_id = request.user.id
            pago.actualizado = hoy
            hoyStr = hoy.strftime('%d/%m/%Y %H:%M')
            pago.seguimiento =  "<b>-" + request.user.username + " a las " + hoyStr + "</b>" + "<br>"
            pago.seguimiento =  pago.seguimiento + "&nbsp Procesó pago por: " + strMonto_procesar +"<br>"
            pago.tipo = 1
    
            # guardar el pago
            form.save()
            # asignar el id del pago guardado
            xPago_id = pago.id

            # Buscar los docuemntos con saldo del cliente 
            xDocumentos = Documento.objects.annotate(saldo = F('monto') - F('abonado')).filter(saldo__gt=0).filter(cliente=id)
            # Preparar monto a procesar
            xMonto_procesar = round(Decimal((request.POST['monto_procesar'])),2)

            # actualizar los documentos afectados, campo abonado en los docuemntos   
            for xDocumento in xDocumentos:
                # si monto a procesar cubre el saldo del docuemnto
                if xMonto_procesar >= xDocumento.saldo:
                   xAbono = xDocumento.saldo
                   xDocumento.abonado = xDocumento.abonado + xAbono 
                # el monto a procesar no cubre el saldo del documento
                else:
                   xAbono = xMonto_procesar  
                   xDocumento.abonado = xDocumento.abonado + xAbono
                   xAbono = xMonto_procesar
                
                # guardar detelle del pago
                detalle = Pago_detalle(pago_id = xPago_id, documento_id =  xDocumento.id, monto_procesar = xAbono)  
                detalle.save()
                # actualizar el abonado del documento
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
            
            # si hay excedente 
            if xMonto_procesar > 0:
                print("-------------Fac: " ,xDocumento.numero,"----------------")
                xAbono = xMonto_procesar  
                xDocumento.abonado = xDocumento.abonado + xAbono
                print(xDocumento.abonado )
                
                xDocumento.pago = pago.id
                print(xDocumento.pago,"***** Duda")
                
                # Guardar detelle del pago
                detalle = Pago_detalle(pago_id = xPago_id, documento_id =  xDocumento.id, monto_procesar = xAbono)  
                detalle.save()
                
                xDocumento.save()
               
                # guardar el excedente
                xExcedente = (xDocumento.monto - xDocumento.abonado) * -1
                xE = Excedente(
                            cli_id = xDocumento.cliente_id,
                            doc_id= xDocumento.id,
                            concepto = "Excedente ",
                            monto=xExcedente,
                            saldo=xExcedente,
                            usuario_id=request.user.id
                        )
                xE.save()
   
                print("xMonto_procesar: " ,xMonto_procesar)
                print("Saldo: " ,xDocumento.saldo)
                xMonto_procesar = xMonto_procesar - xAbono
                print("xAbono: " ,xAbono)
                print("Monto restante",  xMonto_procesar )
                print("--------- Sobro monto_procesar ----------")
            
            return redirect('cobranza', id, 0, 0, 0)
        
        else:
            messages.error(
                request, "Su operación no se puedo efectuar debido a problemas en el Servidor. El formulario no es válido")
    
    context = {
        'xUsuario':xUsuario,
        'form': form,
        'xFormas': xFormas,
        'xTasa': xTasa,
        'xId': xId,
        'xCliente': xCliente,
        'xBancosdestino': xBancosdestino
    }
    return render(request, 'app_gestion/pago_cuenta.html', context)

   
# validar referencia de pago
def Validar_referenciaView(request):
    data = {'status': True}
    # print('Dato: ',request.POST.get('campo'))
   
    # para campos repetidos
    xRegistros = Pago.objects.filter(referencia=request.POST.get('campo'))
    if xRegistros.exists():
        print("Resgistros encontados: ", xRegistros.count())
    else:
        data = {'status': False}
    
    return JsonResponse(data, safe=False)

# cargar bancos destinos
def Cargar_bancosView(request):
    # print('Dato: ',request.POST.get('campo'))
    xBancosdestino = BancoDestino.objects.exclude(id=6).filter(tipo=request.POST.get('campo')).values('id','nombre')
    data = list(xBancosdestino)
    return JsonResponse(data, safe=False)


@login_required
def Estado_cuentaView(request, id, desde, fecha_ini, fecha_fin):
    xUsuario = request.user

    xClientes = Cliente.objects.all()

    if desde == 'cobranza':
        xCliente = Cliente.objects.get(id=id)
        xCliente_nombre = xCliente.nombre
    else:
        xCliente_nombre = ""
    xId = id

    if request.method == 'GET':
        print("--------- Parametros recibidos GET ----------") 
        fecha_ini  = date.today() - timedelta(days=60)
        fecha_fin  = date.today() 
   
        xFecha_ini = fecha_ini.strftime('%Y-%m-%d')
        xFecha_fin = fecha_fin.strftime('%Y-%m-%d')
        xFecha_corte_ini  = fecha_ini - timedelta(days=1)
    else:  
        print("--------- Parametros recibidos POST ----------")
        xFecha_ini = fecha_ini
        xFecha_fin = fecha_fin 

        xFecha_corte_ini = datetime.strptime(fecha_ini, '%Y-%m-%d') - timedelta(days=1)
        
    # Buscar saldo del corte
    print("******* buscando todos desde el inicio los documentos con fecha menor o igaul ka fecha Hasta ******** ", xFecha_corte_ini)
    qD= Documento.objects.filter(cliente=id).filter(fecha__lte=xFecha_corte_ini).values('id','numero','fecha','monto','creado')
    qP = Pago.objects.filter(cliente=id).filter(fecha__lte=xFecha_corte_ini).values('id','referencia','fecha','monto_procesar', 'forma__forma','creado')
    # Prepara lista de datos    
    xSaldo_final = Decimal(0) # reiniciar saldo
    balance = round(xSaldo_final, 2)
    data_lista1 = []
    for xAsiento in qD:
        xAsiento["documento"] = xAsiento['numero']
        xAsiento["forma"] = "-"
        xAsiento["dc"] = "+"
        xAsiento["monto_m"] = xAsiento['monto']
        xAsiento["hora"] = xAsiento['creado'].time()
        data_lista1.append(xAsiento) # Se agrega cada registro a la lista

    for xAsiento in qP:
        xAsiento["documento"] = xAsiento['referencia']
        xAsiento["forma"] = xAsiento['forma__forma']
        xAsiento["dc"] = "-"
        xAsiento["monto_m"] = xAsiento['monto_procesar']
        xAsiento["hora"] = xAsiento['creado'].time()
        # print(xAsiento["documento"][0:20])
        if xAsiento["documento"][0:20] != "Abono excedente Doc:": # si la referencia del abono no es excedente
            data_lista1.append(xAsiento) # Se agrega cada registro a la lista

    # Ordeno la lista obtenida
    data_lista_ordenada1 = sorted(data_lista1, key=itemgetter('fecha','hora'))

    # Calculo el saldo balance    
    for key in data_lista_ordenada1:
        if key['dc'] == "+":
            balance = balance + key['monto_m']
        else:
            balance = balance - key['monto_m']
        
        key['balance'] = balance
        print(key['balance'])
 
    xSaldo_final = balance
    print("Saldo final del corte es  ====================>", xSaldo_final)
 
    # ahora si obtengo los documentos a mostrar
    qDocumentos = Documento.objects.filter(cliente=id).filter(fecha__range=(fecha_ini, fecha_fin)).values('id','numero','fecha','monto','creado','abonado')
    # obtengo los pagos
    qPagos = Pago.objects.filter(cliente=id).filter(fecha__range=(fecha_ini, fecha_fin)).values('id','fecha','monto_procesar', 'forma__forma','referencia','creado', 'banco_destino__nombre')
  
    balance = round(xSaldo_final, 2)
    data_lista = []
    # data_lista.append({"fecha": fecha_ini, "hora": date_object, "documento": "Saldo incial del periodo", "forma": "", "dc":"", "monto_m":0})
    for xAsiento in qDocumentos:
        xAsiento["documento"] = xAsiento['numero']
        xAsiento["forma"] = "-"
        xAsiento["des"] = "-"
        xAsiento["dc"] = "+"
        xAsiento["monto_m"] = xAsiento['monto']
        xAsiento["hora"] = xAsiento['creado'].time()
        data_lista.append(xAsiento) # Se agrega cada registro a la lista
  
    for xAsiento in qPagos:
        xAsiento["documento"] = xAsiento['referencia']
        xAsiento["forma"] = xAsiento['forma__forma']
        xAsiento["des"] = xAsiento['banco_destino__nombre']
        xAsiento["dc"] = "-"
        xAsiento["monto_m"] = xAsiento['monto_procesar']
        xAsiento["hora"] = xAsiento['creado'].time()
        # print(xAsiento["documento"][0:20])
        if xAsiento["documento"][0:20] != "Abono excedente Doc:": # si la referencia del abono no es excedente
            data_lista.append(xAsiento) # Se agrega cada registro a la lista
    
    # Ordeno la lista obtenida
    data_lista_ordenada = sorted(data_lista, key=itemgetter('fecha','hora'))

    # Calculo el saldo balance    
    for key in data_lista_ordenada:
         if key['dc'] == "+":
            balance = balance + key['monto_m']
         else:
            balance = balance - key['monto_m']
         
         key['balance'] = balance
        #  print("balance:",key['balance'])
    

    context = {
        'xUsuario': xUsuario,
        'xCliente_nombre': xCliente_nombre ,
        'xClientes': xClientes,
        'xId':xId,
        'xDesde': desde,
        'xFecha_ini':xFecha_ini,
        'xFecha_fin': xFecha_fin,
        'xAsientos': data_lista_ordenada,
        'xSaldo_inicial': xSaldo_final

    }
 
    return render(request, 'app_gestion/estado_de_cuenta.html', context)

# validar mumero de documento
def Validar_numeroView(request):
    # print('campo: ',request.POST.get('campo'))
    
    # para campos unicos
    data = {'status': True}
    try:
        xRegistro = Documento.objects.get(numero=request.POST.get('campo'))
        print("Encontrado el Documento: ",xRegistro)
    except Documento.DoesNotExist:
        data = {'status': False}
    
    return JsonResponse(data, safe=False)


@login_required
def Actualizar_fechasView(request):
    # parametros
    id =  request.POST.get('campo')
    data = {'status': True}
    f = request.POST.get('f')
    v = request.POST.get('v')
    fecha_actual = datetime.now()
    # Obtengo el registro a editar
    try:
        documento = Documento.objects.get(id=id)
        # print("Encontrado el Documento: ",documento.id)
    except documento.DoesNotExist:
        data = {'status': False}
    
    # actualizo las fechas
    documento.fecha = f
    documento.vencimiento = v
    # Convierto la fecha str a objeto de fecha
    fecha_v = datetime.strptime(v, '%Y-%m-%d')
    # Resto la fecha de veneciemto de la fecha actual
    diferencia = fecha_v - fecha_actual 
    documento.dias_v = diferencia.days  + 1
    # Actualizo dias de credito
    fecha_f = datetime.strptime(f, '%Y-%m-%d')
    dias_creito  =  fecha_v - fecha_f
    documento.credito = dias_creito.days 
          
    documento.save()
    
    return JsonResponse(data, safe=False)
    
# validar ced_rif del cliente
def Validar_clienteView(request):
    data = {'status': True}
    # print('Dato: ',request.POST.get('campo'))
   
    # para campos repetidos
    xRegistros = Cliente.objects.filter(ced_rif=request.POST.get('campo'))
    if xRegistros.exists():
        print("Resgistros encontados: ", xRegistros.count())
    else:
        data = {'status': False}
    
    return JsonResponse(data, safe=False)


# agregar ciudad desde agregar cliente
def agregar_ciudad_desde_agregar_vendedorView(request):
    xUsuario = request.user
    xR = Ciudad(ciudad = request.POST.get('ciudad'), estado_id = request.POST.get('estado') )
    xR.save()
    data = {'id': xR.id}
    return JsonResponse(data, safe=False)
    
# obtener ciudad - ajax para obtener las ciudades -
def obtener_ciudadesView(request):
    xUsuario = request.user
    #provee_id = request.POST.get('id')
    qCiudades = Ciudad.objects.all()
    xCiudades = qCiudades.values('id','ciudad')
    data = list(xCiudades)
    return JsonResponse(data, safe=False)

# agregar vendedor desde agregar cliente
def agregar_vendedor_desde_agregar_clienteView(request):
    xUsuario = request.user
   
    data = {'id': 0}
    xCedula = "V" + request.POST.get('m_cedula')
    try:
        buscar_vendedor = Vendedor.objects.get(cedula=xCedula)
        print("Encontrado el Vendedor: ", buscar_vendedor)
    except Vendedor.DoesNotExist:
        # print("==========================",request.POST.get('m_ciudad'))
        xR = Vendedor(cedula = xCedula, nombre = request.POST.get('m_nombre'), ciudad_id = request.POST.get('m_ciudad'))
        xR.save()
        data = {'id': xR.id}

    return JsonResponse(data, safe=False)

# obtener vendedor - ajax para obtener las vendedores -
def obtener_vendedoresView(request):
    xUsuario = request.user
    qVendedores = Vendedor.objects.filter(status_id=1).order_by('nombre')
    xVendedores = qVendedores.values('id','nombre')
    data = list(xVendedores)
    return JsonResponse(data, safe=False)


@login_required
def estado_cuentas_detalle_docView(request, id, xDoc, xMonto):
    xUsuario = request.user

    xDoc = xDoc
    xMonto = Decimal(xMonto)
  
    # print(xMonto)
    xPagos_detalle = Pago_detalle.objects.filter(documento_id = id).values('documento__fecha','pago__fecha', 'monto_procesar','pago__referencia','pago__forma__forma').order_by('pago__fecha', 'id')
   
    xFecha = xPagos_detalle[0]["documento__fecha"]
    data_lista = []
    data_lista.append({"fecha":xFecha, "referencia": xDoc, "forma": "-", "pago": 0, "monto": "-","balance": xMonto })
    # print("----------- Encabezado ------------------")
    # print(data_lista)
    primero = True
    balance = xMonto
    for xDetalle in xPagos_detalle:
        # print("----------- Detalle ------------------")
        # print(data_lista)
              
        xDetalle["fecha"] = xDetalle["pago__fecha"] 
        xDetalle["referencia"] = xDetalle["pago__referencia"]
        xDetalle["forma"] = xDetalle["pago__forma__forma"]
        xDetalle["monto"] = xDetalle["monto_procesar"]
      
        balance -= xDetalle["monto_procesar"]
        xDetalle["balance"] = balance
        data_lista.append(xDetalle) # Se agrega cada registro a la lista
        

    # print(data_lista)
        
    context = {
        'xUsuario': xUsuario,
        'xPagos_detalle': data_lista,
        'xDoc': xDoc,
    }
    
    return render(request, 'app_gestion/estado_cuentas_detalle_doc.html', context)

# agregar cliente desde agregar docuemnto
def agregar_cliente_desde_agregar_documentoView(request):
    xR = Cliente(ced_rif = request.POST.get('ced_rif'), nombre = request.POST.get('nombre'), vendedor_id = request.POST.get('vendedor_id'), usuario_id=request.user.id)
    xR.save()
    data = {'id': xR.id}
    return JsonResponse(data, safe=False)

# obtener clientes- ajax para obtener los clientes -
def obtener_clientesView(request):
    xUsuario = request.user
    #provee_id = request.POST.get('id')
    qClientes = Cliente.objects.all()
    xClientes = qClientes.values('id','nombre')
    data = list(xClientes)
    return JsonResponse(data, safe=False)


@login_required
def VendedoresView(request, xStatus, xCiudad):
    xUsuario = request.user
    # print("--------- Parametros recibidos GET ----------")
  
    xStatu_seleccionado = xStatus
    xCiudad_seleccionado  = xCiudad
    xExcluidos = [2, 4]
    xStatus_select = Statu.objects.exclude(id__in=xExcluidos)
    xCiudades = Ciudad.objects.all()

    if request.method == 'POST':
        # print("--------- Parametros recibidos POST ----------")
        xStatu_seleccionado  = request.POST.get('f_status')
        xCiudad_seleccionado = request.POST.get('f_ciudad')

    qVendedores= Vendedor.objects.values('id','cedula','nombre','ciudad__ciudad','status__statu').order_by("nombre")

    if xStatus == 0  and xCiudad == 0:
        xVendedores=qVendedores
    elif xStatus != 0 and xCiudad != 0:
        xVendedores=qVendedores.filter(status_id=xStatus, ciudad_id = xCiudad)
    elif xStatus != 0 and xCiudad == 0:
        xVendedores=qVendedores.filter(status_id=xStatus)
    elif xStatus == 0 and xCiudad != 0:
        xVendedores=qVendedores.filter(ciudad_id = xCiudad)

   
    context = {
        'xUsuario': xUsuario,
        'xVendedores': xVendedores,
        'xStatus_select':xStatus_select,
        'xStatu_seleccionado': int(xStatu_seleccionado),
        'xCiudades': xCiudades,
        'xCiudad_seleccionado': int(xCiudad_seleccionado),
   
    }
    return render(request, 'app_gestion/vendedores.html', context)


@login_required
def add_vendedorView(request):
    # xUsuario = request.user
    xOpcion = "Agregando"
     
    xPrefijos_cedula = Prefijo_ced_rif.objects.all()
    xCiudades = Ciudad.objects.all()
    xEstados = Estado.objects.all()
       
    form = agregar_vendedorForm()

    if request.method == 'POST':
        form = agregar_vendedorForm(request.POST)

        request.POST._mutable = True
        request.POST['status'] = 1
        request.POST['cedula'] = request.POST['prefijo_r'] + request.POST['cedula'] 
       
        # for field in form:
        #       print("Field:", field.name, "-> ", field.errors)
    
        if form.is_valid():
            vendedor = form.save(commit=False)
            vendedor.usuario_id = request.user.id
            vendedor.save()

            # Limpiara formulario para otro
            form = agregar_vendedorForm()
            context = {
               'form': form,
               'xOpcion': xOpcion,
               'xPrefijos_cedula':xPrefijos_cedula,
               'xCiudades': xCiudades,
               'xEstados': xEstados,
               'rNum_cedula': "",
               'otro': True,
            }

            return render(request, 'app_gestion/vendedores_crud.html', context)
        else:
            messages.error(
                request, "Su operación no se puedo efectuar debido a problemas en el Servidor. El formulario no es válido")
    
    context = {
      'form': form,
      'xOpcion': xOpcion,
      'xPrefijos_cedula':xPrefijos_cedula,
      'xCiudades': xCiudades,
      'xEstados': xEstados,
      'rNum_cedula': "",
      'otro': False  
    }
    return render(request, 'app_gestion/vendedores_crud.html', context)


@login_required
def Editar_vendedorView(request, id):
    xUsuario = request.user
    xOpcion = "Editando"
   
    xPrefijos_cedula = Prefijo_ced_rif.objects.all()
    xCiudades = Ciudad.objects.all()
    xExcluidos = [2, 4]
    xStatus = Statu.objects.exclude(id__in=xExcluidos)
    
    # Obtengo el registro a editar
    xVendedor = Vendedor.objects.get(id=id)
    rPre_Cedula = xVendedor.cedula[0:1]
    rCedula = xVendedor.cedula[1:]
    rCiudad = xVendedor.ciudad.id
    rStatu = xVendedor.status.id
    rNum_cedula = xVendedor.cedula
  
    form = agregar_vendedorForm(instance=xVendedor)

    if request.method == 'POST':
        form = agregar_vendedorForm(request.POST, instance=xVendedor)
        # request.POST._mutable = True
    
        # for field in form:
        #      print("Field:", field.name, "-> ", field.errors)
        
        if form.is_valid():
            vendedor = form.save(commit=False)
            vendedor.cedula = request.POST.get('prefijo_r') + request.POST.get('cedula')
            vendedor.save()
            return redirect('vendedores',1,0)
        else:
            messages.error(
                request, "Su operación no se puedo efectuar debido a problemas en el Servidor. El formulario no es válido")

    context = {
        'form': form,
        'xOpcion': xOpcion,
        'xPrefijos_cedula': xPrefijos_cedula,
        'rPre_Cedula': rPre_Cedula,
        'rCedula': rCedula,
        'xCiudades': xCiudades,
        'rCiudad': rCiudad,
        'xStatus': xStatus,
        'rStatu': rStatu,
        'rNum_cedula': rNum_cedula
    }
    return render(request, 'app_gestion/vendedores_crud.html', context)



# validar mumero de documento
def Validar_vendedorView(request):
    # print('campo: ',request.POST.get('campo'))
    
    # para campos unicos
    data = {'status': True}
    try:
        xRegistro = Vendedor.objects.get(cedula=request.POST.get('campo'))
        print("Encontrado el registro: ",xRegistro)
    except Vendedor.DoesNotExist:
        print("NO Encontrado el registro")
        data = {'status': False}
    
    return JsonResponse(data, safe=False)

def MigrarView(request):
    xUsuario = request.user

    if request.method == 'POST':
   
        csv_file = request.FILES['file']
        registros = []
        with open("C:/Users/sandr/Downloads/"+str(csv_file), "r") as csv_file:
            data = list(csv.reader(csv_file, delimiter=";"))
            
            for row in data[1:]:
                 registros.append(
                     Ciudad(
                         ciudad = row[0],
                         estado_id = row[1],
                    
                     )
                 )

        if len(registros) > 0:
            Ciudad.objects.bulk_create(registros)
           
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'El archivo no es válido')

        return redirect('inicio')
    
    context = {
    'xUsuario': xUsuario,
    }

    return render(request, 'app_gestion/migrar.html', context)


@login_required
def Cobranza_vendedorView(request, xVendedor,  fecha_fin):


    xUsuario = request.user
    if xVendedor != 0:
        xVendedor_seleccionado = xVendedor
    else:
        xVendedor_seleccionado   = 0

    xVendedores = Vendedor.objects.filter(status_id=1).order_by('nombre')

    actualizar_dias_vencido()
    
    if request.method == 'GET':
        # print("--------- Parametros recibidos GET ----------") 
        # fecha_ini  = date.today() 
        # xFecha_ini = fecha_ini.strftime('%Y-%m-%d')
        fecha_fin  = date.today() + timedelta(days=5)
        xFecha_fin = fecha_fin.strftime('%Y-%m-%d')
        qDocumentos = Documento.objects.annotate(saldo = F('monto') - F('abonado')).filter(saldo__gt=0)
        
    else:  
        # print("--------- Parametros recibidos POST ----------")
        xFecha_fin = fecha_fin
        qDocumentos = Documento.objects.annotate(saldo = F('monto') - F('abonado')).filter(saldo__gt=0).filter(cliente_id__vendedor__id=xVendedor, vencimiento__lte=xFecha_fin).values('id','cliente_id','numero','credito','fecha','dias_v','vencimiento','monto','cliente_id__vendedor__id','abonado','saldo','cliente__nombre').order_by('cliente__nombre').order_by('vencimiento')
    
        # for x in qDocumentos:
        #  print("Documento ",x['numero'],x['vencimiento'])
        #  print(qDocumentos[0]['vencimiento'])
    
        # if qDocumentos.exists():
        #     fecha_ini = qDocumentos[0]['vencimiento'] # fecha de vencimento del docuemto mas viejo 
        #     xFecha_ini = fecha_ini.strftime('%Y-%m-%d')
        # else:
        #     fecha_ini  = date.today() 
        #     xFecha_ini = fecha_ini.strftime('%Y-%m-%d')

    xDocumentos=qDocumentos.filter(cliente_id__vendedor__id=xVendedor)

    context = {
        'xUsuario': xUsuario,
        'xDocumentos': xDocumentos,
        'xVendedores': xVendedores,
        'xVendedor_seleccionado': int(xVendedor_seleccionado),
        # 'xFecha_ini': xFecha_ini,
        'xFecha_fin': xFecha_fin,
    }

    # HTML('app_gestion/cobranza_vendedor.html').write_pdf('mi_documento.pdf')
    return render(request, 'app_gestion/cobranza_vendedor.html', context)
 

@login_required
def historial_pagosView(request, xCliente, fecha_ini, fecha_fin):
    xUsuario = request.user
    if xCliente != 0:
         xCliente_seleccionado = xCliente
    else:
        xCliente_seleccionado   = 0
    
    xClientes = Cliente.objects.all()
    
    if request.method == 'GET':
        # print("--------- Parametros recibidos GET ----------") 
        fecha_ini  = date.today() - timedelta(days=90)
        fecha_fin  = date.today() 
        xFecha_ini = fecha_ini.strftime('%Y-%m-%d')
        xFecha_fin = fecha_fin.strftime('%Y-%m-%d')
    else:  
        # print("--------- Parametros recibidos POST ----------")
        xFecha_ini = fecha_ini
        xFecha_fin = fecha_fin 
    
    qPagos=Pago.objects.filter(fecha__range=(fecha_ini, fecha_fin)).values('id','cliente_id','referencia','fecha','monto','monto_procesar','forma__forma', 'tasa','cliente__nombre','observacion', 'seguimiento', 'forma_id','banco_destino__nombre','tipo','creado').order_by('-fecha', '-creado')
    
    if xCliente == 0 :
       xPagos=qPagos.all()
    else:
        xPagos=qPagos.filter(cliente_id=xCliente)

    context = {
        'xUsuario': xUsuario,
        'xPagos': xPagos,
        'xClientes': xClientes,
        'xCliente_seleccionado': int(xCliente_seleccionado),
        'xFecha_ini': xFecha_ini,
        'xFecha_fin': xFecha_fin,
     }
 
    return render(request, 'app_gestion/historial_pagos.html', context)


@login_required
def Pago_documentosView(request, id, cliente):
    xUsuario = request.user
    xCliente = cliente
    xId = id
 
    xFormas = PagoForma.objects.order_by('orden').exclude(id=5)
    xBancosdestino = BancoDestino.objects.exclude(id=6)
  
    xTasas = Tasa.objects.all()
    if xTasas.exists():
        xTasa = str(xTasas[0].monto)
    else:
        messages.error(
            request, "No ha fijado ninguna tasa de cambio")
        return redirect('inicio')

    form = asentar_pagoForm(request.POST)
    if request.method == 'POST':
 
        # preparando los campos dependeindo de que forma de pago 
        request.POST._mutable = True
        if request.POST['monto'] == "":
            request.POST['monto'] = "0,00"

        if request.POST['banco_destino'] == "":
            request.POST['banco_destino'] = "6"
      
        if request.POST['referencia'] == "":
            request.POST['referencia'] = "-"

        request.POST['monto'] = quitarFormato(request.POST['monto'])
        request.POST['tasa'] = quitarFormato(request.POST['tasa'])
        request.POST['monto_procesar'] = quitarFormato(request.POST['monto_procesar'])
        strMonto_procesar = darFormato(request.POST['monto_procesar'])

        hoy = datetime.now()
             
        if form.is_valid():
            # recorrer el post para ver que documentos traen abono 
            for elemento in request.POST: # iterando todo el POST
                if ((elemento[0:15]) == "monto_ingresado"): # si el elemento es un monto
                     xDoc_Id = elemento[16:len(elemento)]
                     xVal = request.POST['monto_ingresado-'+str(xDoc_Id)]
                     if xVal != '' and xVal != '0,00': # Si el monto trae valor se procesa el pago
                        xDoc_Id = elemento[16:len(elemento)]
                        xMonto_ingresado = quitarFormato(request.POST['monto_ingresado-'+str(xDoc_Id)])
                        # actualizo el abonado del documento
                        documento = Documento.objects.get(id=xDoc_Id)
                        documento.abonado = documento.abonado + Decimal(xMonto_ingresado)
                        documento.save() 
                        # guardar el pago
                        pago = form.save(commit=False)
                        pago.cliente_id = id
                        pago.usuario_id = request.user.id
                        pago.actualizado = hoy
                        hoyStr = hoy.strftime('%d/%m/%Y %H:%M')
                        pago.seguimiento=  "<b>-" + request.user.username + " a las " + hoyStr + "</b>" + "<br>"
                        pago.seguimiento=  pago.seguimiento + "&nbsp Procesó pago por: " + strMonto_procesar +"<br>"
                        pago.tipo = 2 # documento
                       
                        form.save() 
                        # asignar el id del pago guardado
                        xPago_id = pago.id
                        # guardar detelle del pago
                        detalle = Pago_detalle(pago_id = xPago_id, documento_id = xDoc_Id, monto_procesar = Decimal(xMonto_ingresado))  
                        detalle.save()
                        
            return redirect('cobranza', id, 0, 0, 0)
                    
        else:
            messages.error(
                request, "Su operación no se puedo efectuar debido a problemas en el Servidor. El formulario no es válido")
    
    context = {
        'xUsuario':xUsuario,
        'form': form,
        'xFormas': xFormas,
        'xTasa': xTasa,
        'xId': xId,
        'xCliente': xCliente,
        'xBancosdestino': xBancosdestino
    }
    return render(request, 'app_gestion/pago_documentos.html', context)


def obtener_saldosView(request):
    # print(request.POST.get('id'))
    xDocumentos = Documento.objects.filter(cliente_id=request.POST.get('id')).annotate(saldo = F('monto') - F('abonado')).filter(saldo__gt=0).values('id','numero','abonado', 'saldo','vencimiento').order_by('id')
    data = list(xDocumentos)
    # print(data)

    return JsonResponse(data, safe=False)

@login_required
def Guardar_tasaView(request):
    hoy = datetime.now()
    hoyStr = hoy.strftime('%d/%m/%Y %H:%M')
    xTasa = quitarFormato(request.POST.get('tasa'))
    tasa = Tasa(fecha = date.today(), monto = Decimal(xTasa), usuario_id = request.user.id,
                 seguimiento = "<b>-" + request.user.username + " a las " + hoyStr + "</b>" + "<br>" 
                 +  "&nbsp Creada" + "<br>", actualizado = hoy)  
    tasa.save()
    return redirect('inicio')


@login_required
def tasasView(request):
    xUsuario = request.user
    xTasas = Tasa.objects.all()

    context = {
        'xUsuario': xUsuario,
        'xTasas': xTasas,
      
    }
    return render(request, 'app_gestion/tasas.html', context)


@login_required
def Add_tasaView(request):

    xOpcion = "Agregando"
    xUsuario = request.user

    form = tasaForm()
    if request.method == 'POST':
        
        # preparando los campos numericos
        request.POST._mutable = True
        request.POST['monto'] = quitarFormato(request.POST['monto'])
        request.POST['fecha'] = date.today()
        
        form = tasaForm(request.POST)
   
        if form.is_valid():
            hoy = datetime.now()
            hoyStr = hoy.strftime('%d/%m/%Y %H:%M')
            tasa = form.save(commit=False)
            tasa.monto = float(request.POST.get('monto'))
            tasa.usuario_id = request.user.id
            tasa.seguimiento =  "<b>-" + request.user.username + " a las " + hoyStr + "</b>" + "<br>"
            tasa.seguimiento =  tasa.seguimiento +  "&nbsp Creada" + "<br>"
            tasa.actualizado = hoy

            tasa.save()
       
            context = {
                'otro': True,
                'form': form,
                'xOpcion': xOpcion
            }
            #return render(request, 'app_gestion/tasa_crud.html', context)
            return redirect('tasas')
        else:
            messages.error(
                request, "Su operación no se puedo efectuar debido a problemas en el Servidor. El formulario no es válido")

    context = {
        'form': form,
        'otro': False,
        'xOpcion': xOpcion
    }
    return render(request, 'app_gestion/tasas_crud.html', context)


@login_required
def Editar_tasaView(request, id):
    
    xOpcion = "Editando"
    
    # Obtengo el registro a editar
    xTasa = Tasa.objects.get(id=id)

    form = tasaForm(instance=xTasa)
    if request.method == 'POST':
        
        # datos originales 
        oMonto = xTasa.monto

        # preparando los campos numericos
        request.POST._mutable = True
        request.POST['monto'] = quitarFormatoDecimal(request.POST['monto'])
        strMonto = darFormato(request.POST['monto'])
     
        form = tasaForm(request.POST, instance=xTasa)

        if form.is_valid():
            # print(type(request.POST.get('monto')), type(oMonto))
            if request.POST.get('monto') != oMonto:
                # print("entro==================")
                hoy = datetime.now()
                hoyStr = hoy.strftime('%d/%m/%Y %H:%M')
                tasa = form.save(commit=False)
                tasa.seguimiento= tasa.seguimiento+ "<b>-" + request.user.username + " a las " + hoyStr + "</b>" + "<br>"
                tasa.seguimiento= tasa.seguimiento+ "&nbsp Corrigió monto de: "+ darFormato(oMonto) + " a "+ strMonto +"<br>"
                tasa.actualizado = hoy
                form.save()

            return redirect('tasas')
        else:
            messages.error(
                request, "Su operación no se puedo efectuar debido a problemas en el Servidor. El formulario no es válido")

    context = {
        'form': form,
        'xOpcion': xOpcion,
        'editando': True,
    }
    return render(request, 'app_gestion/tasas_crud.html', context)


@login_required
def Pago_cuenta_corregirView(request, id, forma_id):
    xUsuario = request.user
 
    xFormas = PagoForma.objects.order_by('orden').exclude(id=5)
   
    if forma_id == 3:
        xBancosdestino = BancoDestino.objects.exclude(tipo='Nacional')
    elif forma_id == 2:
        xBancosdestino = BancoDestino.objects.exclude(tipo='Inter')
    elif forma_id == 1:
        xBancosdestino = BancoDestino.objects.exclude(tipo='Inter').exclude(id=6)
    elif forma_id == 4:
        xBancosdestino = BancoDestino.objects.exclude(tipo='Inter')
    elif forma_id == 6:
        xBancosdestino = BancoDestino.objects.exclude(tipo='Inter')


    # Obtengo el registro a editar
    xPago = Pago.objects.get(id=id)
    rCliente = Cliente.objects.get(id=xPago.cliente.id)
    rMonto = xPago.monto
    rMonto_procesar = xPago.monto_procesar
    rFormaId = xPago.forma_id
    rForma = PagoForma.objects.get(id=xPago.forma.id)
    rBancodestinoId = xPago.banco_destino_id
    rObjBanco = BancoDestino.objects.get(id=xPago.banco_destino_id)
    rRef = xPago.referencia
      
    xTasas = Tasa.objects.all()
    if xTasas.exists():
        xTasa = str(xTasas[0].monto)
    else:
        messages.error(
            request, "No ha fijado ninguna tasa de cambio")
        return redirect('inicio')
    
    form = asentar_pagoForm(instance=xPago)
    
    if request.method == 'POST':

        # datos originales 
        oFecha = xPago.fecha.strftime('%d/%m/%Y')
        oForma = xPago.forma_id
        oMonto_p = xPago.monto_procesar
        oBanco = xPago.banco_destino_id
        oBamcoStr = rObjBanco.nombre
        oReferencia = xPago.referencia
     
        # Preparando el POST
        request.POST._mutable = True

        request.POST['forma'] = oForma # se mantiene la original, no se puede cambiar

        if request.POST['monto'] == "":
            request.POST['monto'] = "0,00"
        
        if request.POST['banco_destino'] == "":
            request.POST['banco_destino'] = "6"
      
        if request.POST['referencia'] == "":
            request.POST['referencia'] = "-"
        
        # preparando los campos numericos
        request.POST['monto'] = quitarFormato(request.POST['monto'])
        request.POST['tasa'] = quitarFormato(request.POST['tasa'])
        request.POST['monto_procesar'] = quitarFormato(request.POST['monto_procesar'])
        strMonto_procesar = darFormato(request.POST['monto_procesar'])

        form = asentar_pagoForm(request.POST, instance=xPago)
        
        if form.is_valid():
            pago = form.save(commit=False)

            # Grabar cambios en pago.seguimiento
            hay_cambio = False
            Corrigio_monto = False
            hoy = datetime.now()
            hoyStr = hoy.strftime('%d/%m/%Y %H:%M')
            fechaStr = (request.POST.get('fecha')[8:10]+"/"+request.POST.get('fecha')[5:7]+"/"+request.POST.get('fecha')[0:4])
            BancoStr = BancoDestino.objects.get(id=int(request.POST.get('banco_destino')))

            if fechaStr != str(oFecha):
                pago.seguimiento = pago.seguimiento + "<b>-" + request.user.username + " a las " + hoyStr + "<br>" + "</b>"
                hay_cambio = True
                pago.seguimiento = pago.seguimiento + "&nbsp Corrigió fecha de: "+ str(oFecha) + " a "+ fechaStr +"<br>"
     
            nMonto_p = round(Decimal(request.POST.get('monto_procesar')),2)
            if nMonto_p != oMonto_p:
                Corrigio_monto = True
                if hay_cambio == False:
                    pago.seguimiento = pago.seguimiento + "<b>-" + request.user.username + " a las " + hoyStr + "<br>" +  "</b>"
                    hay_cambio = True
                pago.seguimiento =  pago.seguimiento + "&nbsp Corrigió monto de: "+ darFormato(oMonto_p) + " a "+ strMonto_procesar +"<br>"
           
            if int(request.POST.get('banco_destino')) != oBanco:
                if hay_cambio == False:
                    pago.seguimiento = pago.seguimiento + "<b>-" + request.user.username + " a las " + hoyStr + "<br>" +  "</b>"
                    hay_cambio = True
                pago.seguimiento =  pago.seguimiento + "&nbsp Corrigió banco de: "+ oBamcoStr + " a "+ str(BancoStr) +"<br>"

            if request.POST.get('referencia') != oReferencia:
                if hay_cambio == False:
                    pago.seguimiento = pago.seguimiento + "<b>-" + request.user.username + " a las " + hoyStr + "<br>" +  "</b>"
                    hay_cambio = True
                pago.seguimiento =  pago.seguimiento + "&nbsp Corrigió referencia de: "+ oReferencia + " a "+request.POST.get('referencia') +"<br>"

            # actalizar el pago
            pago.cliente_id = xPago.cliente.id
            pago.usuario_id = request.user.id
            pago.actualizado = hoy
            form.save()
            # asignar el id del pago guardado
            xPago_id = pago.id

            if Corrigio_monto == False:
                return redirect('historial_pagos', 0, ' ', ' ')  

            # Reversar los registos de este pago 
            xPago_detalles = Pago_detalle.objects.filter(pago_id=id)
            for xPago_detalle in xPago_detalles:
                 xDoc = Documento.objects.get(id=xPago_detalle.documento_id)
                 xDoc.abonado = xDoc.abonado - xPago_detalle.monto_procesar
                 xDoc.actualizado = hoy
                 xDoc.save()
                #  print("Saldo actualizado a: ",xDoc.abonado, xPago_detalle.monto_procesar)
                 # borrar pago detalle
                 xPago_detalle.delete()
            
            # Borrar el excedente
            try:
                xExc = Excedente.objects.get(doc_id=xPago_detalle.documento_id)
                xExc.delete()
            except Excedente.DoesNotExist:
                # print("No hay excedente")
                pass
           
            # Buscar los docuemntos con saldo del cliente 
            xDocumentos = Documento.objects.annotate(saldo = F('monto') - F('abonado')).filter(saldo__gt=0).filter(cliente=xPago.cliente.id)
            # Preparar monto a procesar
            xMonto_procesar = round(Decimal((request.POST['monto_procesar'])),2)

            # actualizar los documentos afectados, campo abonado en los docuemntos   
            for xDocumento in xDocumentos:
                # si monto a procesar cubre el saldo del docuemnto
                if xMonto_procesar >= xDocumento.saldo:
                   xAbono = xDocumento.saldo
                   xDocumento.abonado = xDocumento.abonado + xAbono 
                # el monto a procesar no cubre el saldo del documento
                else:
                   xAbono = xMonto_procesar  
                   xDocumento.abonado = xDocumento.abonado + xAbono
                   xAbono = xMonto_procesar
                
                # guardar detelle del pago
                detalle = Pago_detalle(pago_id = xPago_id, documento_id =  xDocumento.id, monto_procesar = xAbono)  
                detalle.save()
                # actualizar el abonado del documento
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
            
            # si hay excedente 
            if xMonto_procesar > 0:
                print("-------------Fac: " ,xDocumento.numero,"----------------")
                xAbono = xMonto_procesar  
                xDocumento.abonado = xDocumento.abonado + xAbono
                xDocumento.pago = pago.id
                
                # Guardar detelle del pago
                detalle = Pago_detalle(pago_id = xPago_id, documento_id =  xDocumento.id, monto_procesar = xAbono)  
                detalle.save()
                
                xDocumento.save()
               
                # guardar el excedente
                xExcedente = (xDocumento.monto - xDocumento.abonado) * -1
                xE = Excedente(
                            cli_id = xDocumento.cliente_id,
                            doc_id= xDocumento.id,
                            concepto = "Excedente ",
                            monto=xExcedente,
                            saldo=xExcedente,
                            usuario_id=request.user.id
                        )
                xE.save()
   
                print("xMonto_procesar: " ,xMonto_procesar)
                print("Saldo: " ,xDocumento.saldo)
                xMonto_procesar = xMonto_procesar - xAbono
                print("xAbono: " ,xAbono)
                print("Monto restante",  xMonto_procesar )
                print("--------- Sobro monto_procesar ----------")
 
   
            return redirect('historial_pagos', 0, ' ', ' ')

        else:
            messages.error(
                request, "Su operación no se puedo efectuar debido a problemas en el Servidor. El formulario no es válido")
    
    context = {
        'xUsuario':xUsuario,
        'form': form,
        'xFormas': xFormas,
        'rFormaId': rFormaId,
        'rMonto_procesar': rMonto_procesar,
        'rMonto': rMonto,
        'xTasa': xTasa,
        'rRef': rRef,
        'rCliente': rCliente,
        'rForma': rForma,
        'rFormaId': rFormaId,
        'rBancodestinoId': rBancodestinoId,
        'xBancosdestino': xBancosdestino
    }
    return render(request, 'app_gestion/pago_cuenta_corregir.html', context)





@login_required
def Pago_documentos_corregirView(request, id, forma_id):
    xUsuario = request.user
 
    xFormas = PagoForma.objects.order_by('orden').exclude(id=5)
   
    if forma_id == 3:
        xBancosdestino = BancoDestino.objects.exclude(tipo='Nacional')
    elif forma_id == 2:
        xBancosdestino = BancoDestino.objects.exclude(tipo='Inter')
    elif forma_id == 1:
        xBancosdestino = BancoDestino.objects.exclude(tipo='Inter').exclude(id=6)
    elif forma_id == 4:
        xBancosdestino = BancoDestino.objects.exclude(tipo='Inter')
    elif forma_id == 6:
        xBancosdestino = BancoDestino.objects.exclude(tipo='Inter')


    # Obtengo el registro a editar
    xPago = Pago.objects.get(id=id)
    rCliente = Cliente.objects.get(id=xPago.cliente.id)
    xId = xPago.cliente.id
    rMonto = xPago.monto
    rMonto_procesar = xPago.monto_procesar
    rFormaId = xPago.forma_id
    rForma = PagoForma.objects.get(id=xPago.forma.id)
    rBancodestinoId = xPago.banco_destino_id
    rObjBanco = BancoDestino.objects.get(id=xPago.banco_destino_id)
    rRef = xPago.referencia
      
    xTasas = Tasa.objects.all()
    if xTasas.exists():
        xTasa = str(xTasas[0].monto)
    else:
        messages.error(
            request, "No ha fijado ninguna tasa de cambio")
        return redirect('inicio')
    
    form = asentar_pagoForm(instance=xPago)
    
    if request.method == 'POST':

        # datos originales 
        oFecha = xPago.fecha.strftime('%d/%m/%Y')
        oForma = xPago.forma_id
        oMonto_p = xPago.monto_procesar
        oBanco = xPago.banco_destino_id
        oBamcoStr = rObjBanco.nombre
        oReferencia = xPago.referencia
     
        # Preparando el POST
        request.POST._mutable = True

        request.POST['forma'] = oForma # se mantiene la original, no se puede cambiar

        if request.POST['monto'] == "":
            request.POST['monto'] = "0,00"
        
        if request.POST['banco_destino'] == "":
            request.POST['banco_destino'] = "6"
      
        if request.POST['referencia'] == "":
            request.POST['referencia'] = "-"
        
        # preparando los campos numericos
        request.POST['monto'] = quitarFormato(request.POST['monto'])
        request.POST['tasa'] = quitarFormato(request.POST['tasa'])
        request.POST['monto_procesar'] = quitarFormato(request.POST['monto_procesar'])
        strMonto_procesar = darFormato(request.POST['monto_procesar'])

        form = asentar_pagoForm(request.POST, instance=xPago)
        
        if form.is_valid():
            pago = form.save(commit=False)

            # Grabar cambios en pago.seguimiento
            hay_cambio = False
            hoy = datetime.now()
            hoyStr = hoy.strftime('%d/%m/%Y %H:%M')
            fechaStr = (request.POST.get('fecha')[8:10]+"/"+request.POST.get('fecha')[5:7]+"/"+request.POST.get('fecha')[0:4])
            BancoStr = BancoDestino.objects.get(id=int(request.POST.get('banco_destino')))

            if fechaStr != str(oFecha):
                pago.seguimiento = pago.seguimiento + "<b>-" + request.user.username + " a las " + hoyStr + "<br>" + "</b>"
                hay_cambio = True
                pago.seguimiento = pago.seguimiento + "&nbsp Corrigió fecha de: "+ str(oFecha) + " a "+ fechaStr +"<br>"
     
            nMonto_p = round(Decimal(request.POST.get('monto_procesar')),2)
            if nMonto_p != oMonto_p:
                if hay_cambio == False:
                    pago.seguimiento = pago.seguimiento + "<b>-" + request.user.username + " a las " + hoyStr + "<br>" +  "</b>"
                    hay_cambio = True
                pago.seguimiento =  pago.seguimiento + "&nbsp Corrigió monto de: "+ darFormato(oMonto_p) + " a "+ strMonto_procesar +"<br>"
           
            if int(request.POST.get('banco_destino')) != oBanco:
                if hay_cambio == False:
                    pago.seguimiento = pago.seguimiento + "<b>-" + request.user.username + " a las " + hoyStr + "<br>" +  "</b>"
                    hay_cambio = True
                pago.seguimiento =  pago.seguimiento + "&nbsp Corrigió banco de: "+ oBamcoStr + " a "+ str(BancoStr) +"<br>"

            if request.POST.get('referencia') != oReferencia:
                if hay_cambio == False:
                    pago.seguimiento = pago.seguimiento + "<b>-" + request.user.username + " a las " + hoyStr + "<br>" +  "</b>"
                    hay_cambio = True
                pago.seguimiento =  pago.seguimiento + "&nbsp Corrigió referencia de: "+ oReferencia + " a "+request.POST.get('referencia') +"<br>"

            # actualizar el pago
            pago.cliente_id = xPago.cliente.id
            pago.usuario_id = request.user.id
            pago.actualizado = hoy
            form.save()
            # asignar el id del pago guardado
            xPago_id = pago.id

            if request.POST.get('cambio') == "No":
                print("mo cambio montos")
                return redirect('historial_pagos', 0, ' ', ' ')  

            # Reversar los registos de este pago 
            xPago_detalles = Pago_detalle.objects.filter(pago_id=id)
            for xPago_detalle in xPago_detalles:
                 xDoc = Documento.objects.get(id=xPago_detalle.documento_id)
                 xDoc.abonado = xDoc.abonado - xPago_detalle.monto_procesar
                 xDoc.actualizado = hoy
                 xDoc.save()
                 print("Saldo reverzado: ", xPago_detalle.monto_procesar)
                 # borrar pago detalle
                 xPago_detalle.delete()
            
            # Borrar el excedente
            try:
                xExc = Excedente.objects.get(doc_id=xPago_detalle.documento_id)
                xExc.delete()
                print("marca 1 no hace falta")
            except Excedente.DoesNotExist:
                # print("No hay excedente")
                pass
           
            # recorrer el post para ver que documentos traen abono 
            for elemento in request.POST: # iterando todo el POST
                if ((elemento[0:15]) == "monto_ingresado"): # si el elemento es un monto
                     xDoc_Id = elemento[16:len(elemento)]
                     xVal = request.POST['monto_ingresado-'+str(xDoc_Id)]
                     if xVal != '' and xVal != '0,00': # Si el monto trae valor se procesa el pago
                        xDoc_Id = elemento[16:len(elemento)]
                        xMonto_ingresado = quitarFormato(request.POST['monto_ingresado-'+str(xDoc_Id)])
                        # actualizo el abonado en documento
                        documento = Documento.objects.get(id=xDoc_Id)
                        documento.abonado = documento.abonado + Decimal(xMonto_ingresado)
                        documento.save() 
                        # guardar el pago
                        # pago = form.save(commit=False)
                        # pago.cliente_id = rCliente
                        # pago.usuario_id = request.user.id
                        # pago.actualizado = hoy
                        # hoyStr = hoy.strftime('%d/%m/%Y %H:%M')
                        # pago.seguimiento=  "<b>-" + request.user.username + " a las " + hoyStr + "</b>" + "<br>"
                        # pago.seguimiento=  pago.seguimiento + "&nbsp Procesó pago por: " + strMonto_procesar +"<br>"
                        # pago.tipo = 2 # documento
                        # form.save() 
                        # asignar el id del pago guardado
                        xPago_id = pago.id
                        # guardar detelle del pago
                        detalle = Pago_detalle(pago_id = xPago_id, documento_id = xDoc_Id, monto_procesar = Decimal(xMonto_ingresado))  
                        detalle.save()
          
            if hay_cambio == False:
                pago.seguimiento = pago.seguimiento + "<b>-" + request.user.username + " a las " + hoyStr + "<br>" +  "</b>"
                pago.seguimiento =  pago.seguimiento + "&nbsp Corrigió distribución" + "<br>"
            else:
                pago.seguimiento =  pago.seguimiento + "&nbsp Corrigió distribución" + "<br>"
            form.save()
           

                
   
            return redirect('historial_pagos', 0, ' ', ' ')

        else:
            messages.error(
                request, "Su operación no se puedo efectuar debido a problemas en el Servidor. El formulario no es válido")
    
    context = {
        'xUsuario':xUsuario,
        'form': form,
        'xFormas': xFormas,
        'rFormaId': rFormaId,
        'rMonto_procesar': rMonto_procesar,
        'rMonto': rMonto,
        'xTasa': xTasa,
        'rRef': rRef,
        'rCliente': rCliente,
        'rForma': rForma,
        'rFormaId': rFormaId,
        'rBancodestinoId': rBancodestinoId,
        'xBancosdestino': xBancosdestino,
        'xId': xId, # Clinet
        'id': id
    }
    
    return render(request, 'app_gestion/pago_documentos_corregir.html', context)

def obtener_pagosView(request):
    xPago_detalles = Pago_detalle.objects.filter(pago_id=int(request.POST.get('id'))).values('id','monto_procesar','documento_id', 'pago_id')
    data_lista = []
    for xPago_detalle in xPago_detalles:
            xDoc = Documento.objects.get(id=xPago_detalle['documento_id'])

            xPago_detalle["id"] = xDoc.id
            xPago_detalle["numero"] = xDoc.numero
            xPago_detalle["vencimiento"] = xDoc.vencimiento
            xAbonado  = xDoc.abonado - xPago_detalle['monto_procesar']
            xPago_detalle["saldo"] = xDoc.monto - xAbonado
            xPago_detalle["monto_ingresado"] = xPago_detalle['monto_procesar']

            data_lista.append(xPago_detalle)
    
    data = list(data_lista)
  
    return JsonResponse(data, safe=False)

@login_required
def cerrarView(request):
    logout(request)
    return redirect('/')

@login_required
def historial_pagos_detalle_docView(request, id, xMonto):
    xUsuario = request.user
    
    xPagos_detalle = Pago_detalle.objects.filter(pago_id = id).values('documento__numero','documento__fecha','pago__fecha', 'monto_procesar','pago__referencia','pago__forma__forma').order_by('pago__fecha', 'id')

    xDoc = id
    xMon = xMonto

    context = {
        'xUsuario': xUsuario,
        'xPagos_detalle': xPagos_detalle,
        'xDoc': xDoc,
        'xMon': Decimal(xMon)
    }
    
    return render(request, 'app_gestion/historial_pagos_detalle_doc.html', context)

@login_required
def doc_proView(request, fecha_ini, fecha_fin):
    xUsuario = request.user

    xClientes = Cliente.objects.all()

 

    if request.method == 'GET':
        print("--------- Parametros recibidos GET ----------") 
        # fecha_ini  = date.today() - timedelta(days=60)
        fecha_ini  = date.today() 
        fecha_fin  = date.today() 
   
        xFecha_ini = fecha_ini.strftime('%Y-%m-%d')
        xFecha_fin = fecha_fin.strftime('%Y-%m-%d')
    else:  
        print("--------- Parametros recibidos POST ----------")
        xFecha_ini = fecha_ini
        xFecha_fin = fecha_fin 

        # xFecha_corte_ini = datetime.strptime(fecha_ini, '%Y-%m-%d') - timedelta(days=150)
        
    xDocumentos = Documento.objects.filter(fecha__range=(fecha_ini, fecha_fin)).values('id','numero','fecha','monto','creado','cliente__nombre','creado').order_by('creado')

   

    context = {
        'xUsuario': xUsuario,
        'xFecha_ini':xFecha_ini,
        'xFecha_fin': xFecha_fin,
        'xDocumentos': xDocumentos,

    }
 
    return render(request, 'app_gestion/documentos_proc.html', context)


