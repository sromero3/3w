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
     path('documentos/<int:xCliente>/<int:xDias>/', views.documentosView, name='documentos'),
     path('add_documento/', views.add_documentoView, name='add_documento'),
     path('editar_documento/<int:id>/', views.Editar_documentoView, name='editar_documento'),
     path('eliminar_documento/<int:id>/', views.Eliminar_documentoView, name='eliminar_documento'),
     path('clientes/<int:xStatus>/<int:xVendedor>/', views.ClientesView, name='clientes'),
     path('add_cliente/', views.add_clienteView, name='add_cliente'),
     path('editar_cliente/<int:id>/', views.Editar_clienteView, name='editar_cliente'),
     path('vendedores/<int:xStatus>/<int:xCiudad>/', views.VendedoresView, name='vendedores'),
     path('add_vendedor/', views.add_vendedorView, name='add_vendedor'),
     path('editar_vendedor/<int:id>/', views.Editar_vendedorView, name='editar_vendedor'),
     path('cobranza/<int:xCliente>/<int:xVendedor>/<int:xIva>/<int:xVencido>/', views.cobranzaView, name='cobranza'),
     path('pago_cuenta/<int:id>/<cliente>/', views.Pago_cuentaView, name='pago_cuenta'),
     path('pago_cuenta_corregir/<int:id>/<int:forma_id>/', views.Pago_cuenta_corregirView, name='pago_cuenta_corregir'),
     path('pago_documentos/<int:id>/<cliente>/', views.Pago_documentosView, name='pago_documentos'),
     path('pago_documentos_corregir/<int:id>/<int:forma_id>/', views.Pago_documentos_corregirView, name='pago_documentos_corregir'),
     path('guardar_tasa/', views.Guardar_tasaView, name='guardar_tasa'),
     path('cerrar/', views.cerrarView, name='cerrar'),
     path('pago_reversar/<int:id>/', views.Pago_reversarView, name='pago_reversar'),


     path('tasas/', views.tasasView, name='tasas'),
     path('add_tasa/', views.Add_tasaView, name='add_tasa'),
     path('editar_tasa/<int:id>/', views.Editar_tasaView, name='editar_tasa'),
    #  path('elimina_tasa/<int:id>/', views.Eliminar_tasaView, name='eliminar_tasa'),

    # Variables
    path('editar_variables/', views.editar_variablesView, name='editar_variables'),
     

     # Consultas
     path('estado_cuentas/<int:id>/<desde>/<fecha_ini>/<fecha_fin>/', views.Estado_cuentaView, name='estado_cuenta'),
     path('estado_cuentas_detalle_doc/<int:id>/<xDoc>/<xMonto>/', views.estado_cuentas_detalle_docView, name='estado_cuentas_detalle_doc'),
     path('cobranza_vendedor/<int:xVendedor>/<fecha_fin>/<int:xCliente>/', views.Cobranza_vendedorView, name='cobranza_vendedor'),
     path('historial_pagos/<int:xCliente>/<fecha_ini>/<fecha_fin>/', views.historial_pagosView, name='historial_pagos'),
     path('historial_pagos_detalle_doc/<int:id>/<xMonto>/', views.historial_pagos_detalle_docView, name='historial_pagos_detalle_doc'),
     path('doc_pro/<fecha_ini>/<fecha_fin>/', views.doc_proView, name='doc_pro'),
     path('saldo_favor/<int:xCliente>/<int:xVendedor>/<int:xIva>/<int:xVencido>/', views.saldo_favorView, name='saldo_favor'),

    # Comisiones  
     path('calcular_comision/', views.calcular_comisionView, name='calcular_comision'),
     path('obtener_comisiones_Bs/', views.obtener_comisionesView, name='obtener_comisiones_bs'),
     path('obtener_comisiones_usd/', views.obtener_comisiones2View, name='obtener_comisiones_usd'),
     path('comisiones_calculadas/<int:xVendedor>/', views.comisiones_calculadasView, name='comisiones_calculadas'),
     path('ver_comision/<int:xComi>/', views.ver_comisionView, name='ver_comision'),
     path('rev_comision/<int:xComi>/', views.rev_comisionView, name='rev_comision'),
     path('validar_comision/', views.validar_comisionView, name='validar_comision'),
     path('cerrar_comision/', views.cerrar_comisionView, name='cerrar_comision'),
     path('comisiones_generales/<int:xPeriodo>/', views.comisiones_generalesView, name='comisiones_generales'),


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
     path('obtener_saldos/', views.obtener_saldosView, name='obtener_saldos'),
     path('obtener_pagos/', views.obtener_pagosView, name='obtener_pagos'),
     path('aplicar_descuento/', views.aplicar_descuentoView, name='aplicar_descuento'),
     
     
     # Migrar
    #  path('e/', views.MigrarView, name='migrar'), 
]