from xmlrpc.client import FastMarshaller
from app_gestion.models import *
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

# Quitar formato a los post
def quitarFormato(cifra):
    # print(cifra)
    monto_numerico = cifra.replace('.', '')
    monto_numerico2 = monto_numerico.replace(',', '.')
    #print("convertido",monto_numerico2)
    return float(monto_numerico2)