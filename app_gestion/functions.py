from xmlrpc.client import FastMarshaller
from app_gestion.models import *
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.db.models import F
from decimal import Decimal
from django.db.models import Subquery
from collections import defaultdict
from django.db.models import Sum

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

    return 

def buscar_fecha_pagado(doc_id):
    # Subquery para obtener el último pago__fecha
    ultimo_pago_subquery = Pago_detalle.objects.filter(
        documento_id=doc_id
    ).order_by('-id').values('pago__fecha')[:1]

    # Ejecutamos la subconsulta
    resultado = Pago_detalle.objects.filter(documento_id=doc_id).annotate(
        fecha_ult_pago=Subquery(ultimo_pago_subquery)
    ).values('fecha_ult_pago').first()

    if resultado:
        xFec = resultado['fecha_ult_pago']
        # print('Su último pago fue el:', xFec)
        return {'fecha_ult_pago': xFec}
  

# def buscar_pagos(doc_id):
#     xPago_detalles = Pago_detalle.objects.filter(
#         documento_id=doc_id,
#         pago__forma_id__in=[1, 4]
#     ).values('monto_procesar', 'pago__tasa')

#     pagos_agrupados = defaultdict(Decimal)
#     for xPago_detalle in xPago_detalles:
#         pagos_agrupados[xPago_detalle['pago__tasa']] += (xPago_detalle['monto_procesar']* xPago_detalle['pago__tasa'])

#     resultado_ordenado = sorted(pagos_agrupados.items(), key=lambda x: x[0])

#     return resultado_ordenado

def buscar_pagos(doc_id):
    # Traer el monto total del documento
    doc = Documento.objects.get(id=doc_id)
    monto_total = doc.monto

    # Traer pagos en USD (formas 1 y 4)
    xPago_detalles = Pago_detalle.objects.filter(
        documento_id=doc_id,
        pago__forma_id__in=[1, 4]
    ).values('monto_procesar', 'pago__tasa')

    pagos_agrupados = defaultdict(Decimal)
    monto_acumulado = Decimal('0')

    for xPago_detalle in xPago_detalles:
        monto_procesar = Decimal(xPago_detalle['monto_procesar'])
        tasa = Decimal(xPago_detalle['pago__tasa'])

        # Si ya llegamos al monto del documento, salimos
        if monto_acumulado >= monto_total:
            break

        # Determinar cuánto se puede procesar sin pasarse
        disponible = monto_total - monto_acumulado
        monto_aceptado = min(monto_procesar, disponible)

        pagos_agrupados[tasa] += monto_aceptado * tasa
        monto_acumulado += monto_aceptado

    # Ordenar por tasa
    resultado_ordenado = sorted(pagos_agrupados.items(), key=lambda x: x[0])
    return resultado_ordenado



# def buscar_pagos2(doc_id):
#     pagos_agrupados = (
#         Pago_detalle.objects.filter(
#             documento_id=doc_id,
#             pago__forma_id__in=[2, 3, 7]
#         )
#         .values('documento_id')
#         .annotate(total_monto=Sum('monto_procesar'))
#     )
#     print("Pagos agrupados:", pagos_agrupados)
#     return list(pagos_agrupados)

def buscar_pagos2(doc_id):
    # Sumar pagos válidos
    pagos_agrupados = (
        Pago_detalle.objects.filter(
            documento_id=doc_id,
            pago__forma_id__in=[2, 3, 7]
        )
        .values('documento_id')
        .annotate(total_monto=Sum('monto_procesar'))
    )

    # Si hay resultados
    if pagos_agrupados:
        monto_doc = Documento.objects.get(id=doc_id).monto
        pagos_agrupados[0]['total_monto'] = min(pagos_agrupados[0]['total_monto'], monto_doc)

    return list(pagos_agrupados)



