from django.contrib import admin
from app_gestion.models import *
# Register your models here.

class ClienteEnAmind(admin.ModelAdmin):
    list_display = ("id", "nombre")

class CiudadEnAmind(admin.ModelAdmin):
    list_display = ("id", "ciudad")

admin.site.register(Cliente, ClienteEnAmind)
admin.site.register(Ciudad, CiudadEnAmind)
