from tkinter.tix import Balloon
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import *
from django.utils import timezone
# Create your models here.

class Control(models.Model):
    fecha_control = models.DateField()

    def __str__(self):
        return str(self.fecha_control) # que campo va a retornar al llamar el objeto
    

class Tasa(models.Model):
    fecha = models.DateField()
    monto = models.DecimalField(
        validators=[MinValueValidator(0.01), MaxValueValidator(10000.99)], max_digits=7, decimal_places=2)
    fuente = models.CharField(max_length=30)
    createdo = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.fuente

    class Meta:
        ordering = ["-id"]    


class Siono(models.Model):
    siono = models.CharField(max_length=10)

    def __str__(self):
        return str(self.siono) # que campo va a retornar al llamar el objeto

    class Meta:
        db_table = "app_gestion_siono" # Nombre en PostgreSQL
        verbose_name = "Siono" # Nombre en Admin
        verbose_name_plural = "Siono" # Nombre en Admin plural
        ordering = ["id"]  


class Dia(models.Model):
    dia = models.IntegerField()

    def __str__(self):
        return str(self.dia) # que campo va a retornar al llamar el objeto

    class Meta:
        db_table = "app_gestion_dias" # Nombre en PostgreSQL
        verbose_name = "Dia" # Nombre en Admin
        verbose_name_plural = "Dias" # Nombre en Admin plural
        ordering = ["id"]  


class Credito(models.Model):
    dia = models.IntegerField()

    def __str__(self):
        return str(self.dia) # que campo va a retornar al llamar el objeto

    class Meta:
        db_table = "app_gestion_credito" # Nombre en PostgreSQL
        verbose_name = "Credito" # Nombre en Admin
        verbose_name_plural = "Creditos" # Nombre en Admin plural
        ordering = ["id"]  


class Statu(models.Model):
    statu = models.CharField(max_length=20)

    def __str__(self):
        return str(self.statu) # que campo va a retornar al llamar el objeto

    class Meta:
        db_table = "app_gestion_status" # Nombre en PostgreSQL
        verbose_name = "Statu" # Nombre en Admin
        verbose_name_plural = "Status" # Nombre en Admin plural
        ordering = ["id"]  


class Estado(models.Model):
    estado = models.CharField(max_length=40)    
    def __str__(self):
        return str(self.estado)

    class Meta:
        db_table = "app_gestion_estados"
        verbose_name = "Estado"
        verbose_name_plural = "CiEstados"
        ordering = ["estado"]  

class Ciudad(models.Model):
    ciudad = models.CharField(max_length=40)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)    
    def __str__(self):
        return str(self.ciudad)

    class Meta:
        db_table = "app_gestion_ciudades"
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        ordering = ["ciudad"]  


class Iva(models.Model):
    iva = models.CharField(max_length=10)

    def __str__(self):
        return str(self.iva) # que campo va a retornar al llamar el objeto

    class Meta:
        db_table = "app_gestion_iva" # Nombre en PostgreSQL
        verbose_name = "Iva" # Nombre en Admin
        verbose_name_plural = "Iva" # Nombre en Admin plural
        ordering = ["id"] 

class Condicion(models.Model):
    condicion = models.CharField(max_length=10)

    def __str__(self):
        return str(self.tipo) # que campo va a retornar al llamar el objeto

    class Meta:
        db_table = "app_gestion_condicion" # Nombre en PostgreSQL
        verbose_name = "Condicion" # Nombre en Admin
        verbose_name_plural = "Condicion" # Nombre en Admin plural
        ordering = ["id"] 


class Vendedor(models.Model):
    cedula = models.CharField(max_length=9, unique=True)
    nombre = models.CharField(max_length=40)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE) 
    status = models.ForeignKey(Statu, on_delete=models.CASCADE, default=1)
    creado = models.DateTimeField(auto_now_add=True, null=False)
    actualizado = models.DateTimeField(auto_now_add=True, null=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre) 
    
    class Meta:
        db_table = "app_gestion_vendedores"
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"
        ordering = ["nombre"]  

class Prefijo_ced_rif(models.Model):
    prefijo_r = models.CharField(max_length=1)

    def __str__(self):
        return self.prefijo_r
    
class Prefijo_telefono(models.Model):
    prefijo_t = models.CharField(max_length=4)

    def __str__(self):
        return self.prefijo_t

class Cliente(models.Model):
    ced_rif = models.CharField(max_length=10)
    nombre = models.CharField(max_length=40)
    # telefono = models.CharField(max_length=25)
    # correo = models.CharField(max_length=50,blank=True,null=True)
    # direccion = models.CharField(max_length=300)
    # ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE) 
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    status = models.ForeignKey(Statu, on_delete=models.CASCADE, default=1)
    creado = models.DateTimeField(auto_now_add=True, null=False)
    actualizado = models.DateTimeField(auto_now_add=True, null=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        db_table = "app_gestion_clientes"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["nombre"]  

class Documento(models.Model):
    numero = models.CharField(max_length=40, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    vencimiento = models.DateField()
    dias_v = models.IntegerField(default=0)
    credito = models.IntegerField(default=0)
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    abonado = models.DecimalField(max_digits=8, decimal_places=2,default=0)
    observacion = models.TextField(max_length=1000, blank=True,null=True)
    iva = models.ForeignKey(Iva, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True, null=False)
    actualizado = models.DateTimeField(auto_now_add=True, null=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    condicion = models.ForeignKey(Condicion, on_delete=models.CASCADE)
  
    
    def __str__(self) -> str:
        return self.numero
    
    class Meta:
        db_table = "app_gestion_documentos"
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"
        ordering = ["vencimiento","id"]  


class PagoForma(models.Model):
    forma = models.CharField(max_length=40, default="")
    orden = models.IntegerField()

    def __str__(self):
        return self.forma

class Banco(models.Model):
    cod = models.CharField(max_length=4, default="")
    nombre = models.CharField(max_length=50, default="")

    def __str__(self):
        return str(self.nombre)
    
class BancoDestino(models.Model):
    cod = models.CharField(max_length=4, default="")
    nombre = models.CharField(max_length=50, default="")
    tipo = models.CharField(max_length=15, default="")

    def __str__(self):
        return str(self.nombre)
    
class Pago(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    # documento = models.ForeignKey(Documento, on_delete=models.CASCADE)
    referencia = models.CharField(max_length=30, null=True, blank=True)
    monto = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Monto en Bs.")
    # validators=[MinValueValidator(0.00), MaxValueValidator(999999.99)], 
    monto_procesar = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Monto en $")
    observacion = models.TextField(max_length=250, blank=True)
    forma = models.ForeignKey(PagoForma, on_delete=models.CASCADE, verbose_name="Forma de pago")
    banco_destino = models.ForeignKey(BancoDestino, on_delete=models.CASCADE, verbose_name="Banco destino")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True, null=False)
    actualizado = models.DateTimeField(auto_now_add=True, null=False)
    tasa = models.DecimalField(max_digits=5, decimal_places=2)
  
    def __str__(self):
         return self.id

    class Meta:
        db_table = "app_gestion_pagos"
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
        ordering = ["fecha", "id"]
        #constraints = [
        #    models.UniqueConstraint(fields=["banco", "referencia"], name='asiento_restriccion')
        #]
        # validar_facturaView es el ejemplo

class Pago_detalle(models.Model):
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    monto_procesar = models.DecimalField(max_digits=8, decimal_places=2)
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
    
    db_table = "app_gestion_pagos_detalles"
    verbose_name = "Pagos_detalles"
    verbose_name_plural = "Pagos_detalles"
    ordering = ["id"]

class Excedente(models.Model):
    cli = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    doc = models.ForeignKey(Documento, on_delete=models.CASCADE)
    concepto = models.CharField(max_length=50, null=True, blank=True)
    monto = models.DecimalField(max_digits=9, decimal_places=2)
    saldo = models.DecimalField(max_digits=9, decimal_places=2)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True, null=False)
    actualizado = models.DateTimeField(auto_now_add=True, null=False)




