from tkinter.tix import Balloon
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import *
from django.utils import timezone
# Create your models here.

class C_status(models.Model):
    status = models.CharField(max_length=10)


class Ciudad(models.Model):
    verbose_name_plural = 'Ciudades'
    ciudad = models.CharField(max_length=40, default="")

    def __str__(self):
        return str(self.ciudad)

    class Meta:
        ordering = ["id"]  

class Cliente(models.Model):
    ced_rif = models.CharField(max_length=10)
    nombre = models.CharField(max_length=40)
    telefono = models.CharField(max_length=11)
    direccion = models.TextField(max_length=200)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE) 
    creado = models.DateTimeField(auto_now_add=True, null=False)
    status = models.ForeignKey(C_status, on_delete=models.CASCADE, default=2)
    Observacion = models.TextField(max_length=1000, default="")
    
    # que valor va a retornar al llamar el objeto
    def __str__(self) -> str:
        return self.nombre
