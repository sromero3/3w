from xmlrpc.client import FastMarshaller
from app_gestion.models import *
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.db.models import F
from decimal import Decimal

# Quitar formato a los post
def quitarFormato(cifra):
    # print(cifra)
    monto_numerico = cifra.replace('.', '')
    monto_numerico2 = monto_numerico.replace(',', '.')
    #print("convertido",monto_numerico2)
    return float(monto_numerico2)


# Quitar formato a los post
def quitarFormatoDecimal(cifra):
    # print(cifra)
    monto_numerico = cifra.replace('.', '')
    monto_numerico2 = monto_numerico.replace(',', '.')
    #print("convertido",monto_numerico2)
    return Decimal(monto_numerico2)


# Dar formato a los post 1.559,32
def darFormato(cifra):
    # Formatear el número con dos decimales y convertirlo a string
    numero_formateado = f"{cifra:,.2f}"
    # Reemplazar la coma por un punto y el punto por una coma
    numero_formateado = numero_formateado.replace(',', 'X').replace('.', ',').replace('X', '.')
    return numero_formateado


# Actauliza los dias de vencimiento 
def actualizar_dias_vencido():
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

          print(" se actualiazo dias_v ")
    return 

def buscar_fecha_pagado(doc_id):
    
     # para campos repetidos
    xPago_detalles = Pago_detalle.objects.filter(documento_id=doc_id).values('pago__fecha', 'pago__monto', 'documento_id','pago__forma_id','pago__forma__forma','monto_procesar','pago__tasa')
    if xPago_detalles.exists():
        for xPago_detalle in xPago_detalles:

            return {
                'fecha': xPago_detalle['pago__fecha'],
                'en': xPago_detalle['pago__forma_id'],
                'montoBs': xPago_detalle['pago__monto'],
                'tasa': xPago_detalle['pago__tasa']
            }

    else:
        data = {'status': False}

   
