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
               fecha_v = datetime.strptime(fecha_str, "%d/%m/%Y")
               # Resta la fecha dada de la fecha actual
           
               diferencia = fecha_v - fecha_actual
            #    print("Vence ",fecha_v, "diferencia =======",diferencia)
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
    # print("--------- Parametros recibidos GET ----------")
    # if xStatu != 0:
    #     xCliente_seleccionado = xCliente
    # else:
    #     xCliente_seleccionado  = 0
    xStatu_seleccionado = 1 
    xStatus_select = Statu.objects.all()

    xClientes = Cliente.objects.values('id','ced_rif','nombre','telefono','ciudad__ciudad','status__statu')
   
    context = {
        'xUsuario': xUsuario,
        'xClientes': xClientes,
        'xStatus_select':xStatus_select,
        'xStatu_seleccionado': int(xStatu_seleccionado),

    }
    return render(request, 'app_gestion/clientes.html', context)


#  add cliente
@login_required
def add_clienteView(request):
    # xUsuario = request.user
    xOpcion = "Agregando"
      
    xPrefijos_ced_rif = Prefijo_ced_rif.objects.all()
    xPrefijos = Prefijo_telefono.objects.all()
    xVendedores = Vendedor.objects.all()
    xCiudades = Ciudad.objects.all()
    # xStatus = Statu.objects.all()
       
    form = agregar_clienteForm()

    if request.method == 'POST':
        form = agregar_clienteForm(request.POST)

        request.POST._mutable = True
        request.POST['status'] = 1
       
        # for field in form:
        #       print("Field:", field.name, "-> ", field.errors)
    
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.sciudad_id = request.POST.get('ciudad')
            cliente.ced_rif = request.POST.get('prefijo_r') + request.POST.get('ced_rif')
            cliente.telefono = request.POST.get('prefijo') + request.POST.get('telefono')
            cliente.usuario_id = request.user.id

            cliente.save()

            # Limpiara formulario para otro gasto
            form = agregar_clienteForm()
            context = {
               'form': form,
               'xOpcion': xOpcion,
               'xPrefijos_ced_rif':xPrefijos_ced_rif,
               'xPrefijos':xPrefijos,
               'xVendedores': xVendedores,
               'xCiudades': xCiudades,
            #  'xStatus': xStatus,
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
      'xPrefijos':xPrefijos,
      'xVendedores': xVendedores,
      'xCiudades': xCiudades,
    #   'xStatus': xStatus,
      'otro': False,  
    }
    return render(request, 'app_gestion/clientes_crud.html', context)



@login_required
def docuementosView(request, xCliente, xDias):
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

    qDocumentos = Documento.objects.values('id','numero','fecha','vencimiento','cliente__nombre','monto','iva__iva','cliente_id__ciudad__ciudad','cliente_id__vendedor__nombre', 'cliente_id__vendedor_id','observacion','abonado', 'dias_v').order_by('-id')
   
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


#  add documento
@login_required
def add_documentoView(request):
    # xUsuario = request.user
    xOpcion = "Agregando"
       
    xClientes = Cliente.objects.all()
    xIvas = Iva.objects.all()
    xCredito = Credito.objects.all()
       
    form = agregar_documentoForm()

    if request.method == 'POST':
        form = agregar_documentoForm(request.POST)

        request.POST._mutable = True
        request.POST['monto'] = quitarFormato(request.POST['monto'])
        request.POST['vencimiento'] = datetime.strptime(request.POST['vencimiento'], '%Y-%m-%d')
       
        # for field in form:
        #      print("Field:", field.name, "-> ", field.errors)
    
        if form.is_valid():
            fecha_actual = datetime.now()
            documento = form.save(commit=False)
            documento.usuario_id = request.user.id
            diferencia = request.POST['vencimiento'] - fecha_actual
            documento.dias_v = diferencia.days + 1
            documento.save()

            # Limpiara formulario para otro gasto
            form = agregar_documentoForm()
            context = {
               'form': form,
               'xOpcion': xOpcion,
               'xClientes': xClientes,
               'xIvas': xIvas,
               'otro': True,
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
     'rNum': "",
     'otro': False,  
    }
    return render(request, 'app_gestion/documentos_crud.html', context)


#  editar docuemnto
@login_required
def Editar_documentoView(request, id):
    xUsuario = request.user
    xOpcion = "Editando"
   
    xClientes =  Cliente.objects.all()
    xIvas =  Iva.objects.all()
    
    # Obtengo el registro a editar
    xDocumento = Documento.objects.get(id=id)
    rClienteId = xDocumento.cliente.id
    rIvaId = xDocumento.iva.id
    rNum = xDocumento.numero
   
    form = agregar_documentoForm(instance=xDocumento)

    if request.method == 'POST':
        form = agregar_documentoForm(request.POST, instance=xDocumento)

        request.POST._mutable = True
        print(request.POST['monto'])
        request.POST['monto'] = quitarFormato(request.POST['monto'])
        print(request.POST['monto'])
        request.POST['vencimiento'] = datetime.strptime(request.POST['vencimiento'], '%Y-%m-%d')

        for field in form:
             print("Field:", field.name, "-> ", field.errors)
        
        if form.is_valid():
            fecha_actual = datetime.now()
            documento = form.save(commit=False)
            diferencia = request.POST['vencimiento'] - fecha_actual 
            documento.dias_v = diferencia.days + 1
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
        'rIvaId': rIvaId,
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
    
    xClientes = Cliente.objects.all()
    xIva_seleccionado  = 0
    xIvas = Iva.objects.all()
    xVendedor_seleccionado  = 0
    xVendedores = Vendedor.objects.all()
    
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
        'xCliente_seleccionado': int(xCliente_seleccionado),
        'xIvas': xIvas,
        'xIva_seleccionado': int(xIva_seleccionado),
        'xVendedores': xVendedores,
        'xVendedor_seleccionado': int(xVendedor_seleccionado),
        'xVencido_seleccionado': xVencido_seleccionado,
    }
    
    return render(request, 'app_gestion/cobranza.html', context)

@login_required
def Asentar_pagosView(request, id, cliente):
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
    print(request.POST)
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
   
        
        # for field in form:
        #     print("Field:", field.name, "-> ", field.errors)
        
        if form.is_valid():

            pago = form.save(commit=False)
            pago.cliente_id = id
            pago.usuario_id = request.user.id
            form.save()

            # Actualizar el campo abono en los Asientos 
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
            
            return redirect('cobranza', id, 0, 0, 0)
        
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

   
# validar si un documento ced_rif estste en un condominio
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
def Estado_cuentaView(request, id, cliente, desde):
    xUsuario = request.user
    xCliente = cliente
    xId = id

    xClientes = Cliente.objects.all()
    
    # obtengo los docuemntos
    qDocumentos = Documento.objects.filter(cliente=id).values('id','numero','fecha','monto','creado')
    # obtengo los pagos
    qPagos = Pago.objects.filter(cliente=id).values('id','fecha','monto_procesar', 'forma__forma','referencia','creado')
    
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
        xAsiento["hora"] = xAsiento['creado'].time()
        data_lista.append(xAsiento) # Se agrega cada registro a la lista
  
    for xAsiento in qPagos:
        xAsiento["documento"] = xAsiento['referencia']
        xAsiento["forma"] = xAsiento['forma__forma']
        xAsiento["dc"] = "-"
        xAsiento["monto_m"] = xAsiento['monto_procesar']
        xAsiento["hora"] = xAsiento['creado'].time()
        data_lista.append(xAsiento) # Se agrega cada registro a la lista
  
    data_lista_ordenada = sorted(data_lista, key=itemgetter('fecha','hora'))
        
    for key in data_lista_ordenada:
         if key['dc'] == "-":
            balance = balance - key['monto_m']
         else:
            balance = balance + key['monto_m']
         
         key['balance'] = balance
         
    context = {
        'xUsuario': xUsuario,
        'xCliente': xCliente,
        'xClientes': xClientes,
        'xId':xId,
        'xDesde': desde,
        'xAsientos': data_lista_ordenada
    }
    
    return render(request, 'app_gestion/estado_de_cuenta.html', context)

# validar si un mumero de documento
def Validar_numeroView(request):
    # print('campo: ',request.POST.get('campo'))

    data = {'status': True}
    try:
        buscar_doc = Documento.objects.get(numero=request.POST.get('campo'))
        # print("Encontrado el Documento: ",buscar_doc)
    except Documento.DoesNotExist:
        data = {'status': False}
    
    return JsonResponse(data, safe=False)

#  actualizar fechas
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
          
    documento.save()
    
    return JsonResponse(data, safe=False)
    
# validar si un cliente ced_rif estste
def validar_clienteView(request):
    xUsuario = request.user
    # print('Cedu_rif: ',request.POST.get('ced_rif'))

    data = {'status': True}
    try:
        buscar_cliente = Cliente.objects.get(ced_rif=request.POST.get('ced_rif'))
        print("Encontrado el Proveedor: ",buscar_cliente)
    except Cliente.DoesNotExist:
        data = {'status': False}
    
    return JsonResponse(data, safe=False)

# agregar ciudad desde agregar cliente
def agregar_ciudad_desde_agregar_clienteView(request):
    xUsuario = request.user
    xR = Ciudad(ciudad = request.POST.get('ciudad'))
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
        xR = Vendedor(cedula = xCedula, nombre = request.POST.get('m_nombre'))
        xR.save()
        data = {'id': xR.id}

    return JsonResponse(data, safe=False)

# obtener vendedor - ajax para obtener las vendedores -
def obtener_vendedoresView(request):
    xUsuario = request.user
    qVendedores = Vendedor.objects.all()
    xVendedores = qVendedores.values('id','nombre')
    data = list(xVendedores)
    return JsonResponse(data, safe=False)




