from tkinter.tix import Balloon
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import *
from django.utils import timezone
# Create your models here.


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
        db_table = "app_gestion_dia" # Nombre en PostgreSQL
        verbose_name = "Dia" # Nombre en Admin
        verbose_name_plural = "Dias" # Nombre en Admin plural
        ordering = ["id"]  


class Statu(models.Model):
    statu = models.CharField(max_length=10)

    def __str__(self):
        return str(self.statu) # que campo va a retornar al llamar el objeto

    class Meta:
        db_table = "app_gestion_status" # Nombre en PostgreSQL
        verbose_name = "Statu" # Nombre en Admin
        verbose_name_plural = "Status" # Nombre en Admin plural
        ordering = ["id"]  


class Ciudad(models.Model):
    ciudad = models.CharField(max_length=40)

    def __str__(self):
        return str(self.ciudad)

    class Meta:
        db_table = "app_gestion_ciudades"
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        ordering = ["id"]  


class Iva(models.Model):
    iva = models.CharField(max_length=10)

    def __str__(self):
        return str(self.iva) # que campo va a retornar al llamar el objeto

    class Meta:
        db_table = "app_gestion_iva" # Nombre en PostgreSQL
        verbose_name = "Iva" # Nombre en Admin
        verbose_name_plural = "Iva" # Nombre en Admin plural
        ordering = ["id"] 


class Vendedor(models.Model):
    ced_rif = models.CharField(max_length=10)
    nombre = models.CharField(max_length=40)
    status = models.ForeignKey(Statu, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.nombre) 
    
    class Meta:
        db_table = "app_gestion_vendedores"
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"

class Cliente(models.Model):
    ced_rif = models.CharField(max_length=10)
    nombre = models.CharField(max_length=40)
    telefono = models.CharField(max_length=25)
    correo = models.CharField(max_length=20,blank=True,null=True)
    direccion = models.TextField(max_length=200)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE) 
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    status = models.ForeignKey(Statu, on_delete=models.CASCADE, default=1)
    observacion = models.TextField(max_length=1000,blank=True,null=True)
    creado = models.DateTimeField(auto_now_add=True, null=False)
    
    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        db_table = "app_gestion_clientes"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

class Documento(models.Model):
    numero = models.CharField(max_length=40)
    fecha = models.DateField()
    vencimiento = models.DateField()
    # dias_credito
    monto = models.DecimalField(
        validators=[MinValueValidator(0.00), MaxValueValidator(10000.99)], max_digits=7, decimal_places=2)
    abonado = models.DecimalField(
        validators=[MinValueValidator(0.00), MaxValueValidator(10000.99)], max_digits=7, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    observacion = models.TextField(max_length=1000,blank=True,null=True)
    iva = models.ForeignKey(Iva, on_delete=models.CASCADE, default="Pendiente")
    
    def __str__(self) -> str:
        return self.numero
    
    class Meta:
        db_table = "app_gestion_documentos"
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"
        ordering = ["-vencimiento"]  


