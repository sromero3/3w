from django.contrib import admin
from app_gestion.models import *
# Register your models here.

class SionoEnAmind(admin.ModelAdmin):
    list_display = ("id", "siono")

class DiaEnAmind(admin.ModelAdmin):
    list_display = ("id", "dia")

class StatuEnAmind(admin.ModelAdmin):
    list_display = ("id", "statu")

class ClienteEnAmind(admin.ModelAdmin):
    list_display = ("id", "nombre")

class CiudadEnAmind(admin.ModelAdmin):
    list_display = ("id", "ciudad")

class IvaEnAmind(admin.ModelAdmin):
    list_display = ("id", "iva")

class VendedorEnAmind(admin.ModelAdmin):
    list_display = ("id", "nombre")

class DocumentoEnAmind(admin.ModelAdmin):
    list_display = ("id", "numero")

admin.site.register(Siono, SionoEnAmind)
admin.site.register(Dia, DiaEnAmind)
admin.site.register(Statu, StatuEnAmind)
admin.site.register(Cliente, ClienteEnAmind)
admin.site.register(Ciudad, CiudadEnAmind)
admin.site.register(Iva, IvaEnAmind)
admin.site.register(Vendedor, VendedorEnAmind)
admin.site.register(Documento, DocumentoEnAmind)