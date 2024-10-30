from django.template import Library
from datetime import datetime

register = Library()

# Filtro para dar formato numeros
def darFormato(cifra):
    s1 = "{:,}".format(cifra)
    s2 = s1.replace(',','n')
    s3 = s2.replace('.',',')
    s4 = s3.replace('n','.')
    return (s4)

register.filter("darFormato", darFormato)


# Filtro para rellenar con 0
def rellenar(numero):
    
    filled = str(numero).zfill(8)
    return (filled)

register.filter("rellenar", rellenar)

# 
def resta_fecha(fecha_r):
    fecha_str = fecha_r.strftime('%d/%m/%Y')

    # Convierte la cadena de texto a un objeto de fecha
    # fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
    fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
    # Obtiene la fecha actual
    fecha_actual = datetime.now()
    # Resta la fecha dada de la fecha actual
    diferencia =  fecha - fecha_actual
    return diferencia.days + 1

register.filter("resta_fecha", resta_fecha,)
