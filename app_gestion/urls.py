from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from app_gestion.form import LoginForm

urlpatterns = [
     # Accesos
     path('', views.Index_gestion, name="index_gestion"), # Vista inicial del proyecto

     path('accounts/login/', auth_views.LoginView.as_view(
       authentication_form=LoginForm,
     ), name="login"), 
     #       url     -    vista     -    nombre_u
     path('inicio/', views.InicioView, name='inicio'),
     path('documentos/<int:xCliente>/<int:xDias>/', views.docuementosView, name='documentos'),
     path('add_documento/', views.add_documentoView, name='add_documento'),
     path('editar_documento/<int:id>/', views.Editar_documentoView, name='editar_documento'),
     path('clientes/<int:xStatus>/<int:xVendedor>/', views.ClientesView, name='clientes'),
     path('add_cliente/', views.add_clienteView, name='add_cliente'),
     path('editar_cliente/<int:id>/', views.Editar_clienteView, name='editar_cliente'),
     path('vendedores/<int:xStatus>/<int:xCiudad>/', views.VendedoresView, name='vendedores'),
     path('add_vendedor/', views.add_vendedorView, name='add_vendedor'),
     path('editar_vendedor/<int:id>/', views.Editar_vendedorView, name='editar_vendedor'),
     path('cobranza/<int:xCliente>/<int:xVendedor>/<int:xIva>/<int:xVencido>/', views.cobranzaView, name='cobranza'),
     path('pago_cuenta/<int:id>/<cliente>/', views.Pago_cuentaView, name='pago_cuenta'),
     path('pago_documentos/<int:id>/<cliente>/', views.Pago_documentosView, name='pago_documentos'),
     

     # Consultas
     path('estado_cuentas/<int:id>/<desde>/<fecha_ini>/<fecha_fin>/', views.Estado_cuentaView, name='estado_cuenta'),
     path('estado_cuentas_detalle_doc/<int:id>/<xDoc>/<xMonto>/', views.estado_cuentas_detalle_docView, name='estado_cuentas_detalle_doc'),
     path('cobranza_vendedor/<int:xVendedor>/<fecha_ini>/<fecha_fin>/', views.Cobranza_vendedorView, name='cobranza_vendedor'),
     path('historial_pagos/<int:xCliente>/<fecha_ini>/<fecha_fin>/', views.Historial_pagosView, name='historial_pagos'),

     # ajax
     path('validar_numero/', views.Validar_numeroView, name='validar_numero'), 
     path('validar_referencia/', views.Validar_referenciaView, name='validar_referencia'),
     path('cargar_bancos/', views.Cargar_bancosView, name='cargar_bancos'),
     path('actualizar_fechas/', views.Actualizar_fechasView, name='actualizar_fechas'),
     path('validar_cliente/', views.Validar_clienteView, name='validar_cliente'),
     path('agregar_ciudad_desde_agregar_vendedor/', views.agregar_ciudad_desde_agregar_vendedorView, name='agregar_ciudad_desde_agregar_vendedor'),
     path('obtener_ciudades/', views.obtener_ciudadesView, name='obtener_ciudades'),
     path('agregar_vendedor_desde_agregar_cliente/', views.agregar_vendedor_desde_agregar_clienteView, name='agregar_vendedor_desde_agregar_cliente'),
     path('obtener_vendedores/', views.obtener_vendedoresView, name='obtener_vendedores'),
     path('agregar_cliente_desde_agregar_documento/', views.agregar_cliente_desde_agregar_documentoView, name='agregar_cliente_desde_agregar_documento'),
     path('obtener_clientes/', views.obtener_clientesView, name='obtener_clientes'),
     path('validar_vendedor/', views.Validar_vendedorView, name='validar_vendedor'),

     
     # Migrar
    #  path('e/', views.MigrarView, name='migrar'), 
]