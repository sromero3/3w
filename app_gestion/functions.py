from xmlrpc.client import FastMarshaller
from app_gestion.models import *
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.db.models import F

# Quitar formato a los post
def quitarFormato(cifra):
    # print(cifra)
    monto_numerico = cifra.replace('.', '')
    monto_numerico2 = monto_numerico.replace(',', '.')
    #print("convertido",monto_numerico2)
    return float(monto_numerico2)

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