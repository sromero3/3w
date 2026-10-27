from datetime import date, datetime
from decimal import Decimal

from django.contrib.auth.models import Group, User
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from app_gestion.models import (
    Ciudad,
    Cliente,
    Condicion,
    Documento,
    Estado,
    Iva,
    Statu,
    Vendedor,
)


class ClientesSinCompraViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='gerente', password='test-pass')
        self.status = Statu.objects.create(statu='Activo')
        estado = Estado.objects.create(estado='Estado')
        ciudad = Ciudad.objects.create(ciudad='Ciudad', estado=estado)
        self.vendedor = Vendedor.objects.create(
            cedula='123456',
            nombre='Vendedor',
            ciudad=ciudad,
            status=self.status,
            usuario=self.user,
        )
        self.iva = Iva.objects.create(iva='0')
        self.condicion = Condicion.objects.create(condicion='Contado')
        self.client.force_login(self.user)

    def crear_cliente(self, nombre):
        return Cliente.objects.create(
            ced_rif=f'J{Cliente.objects.count():08d}',
            nombre=nombre,
            vendedor=self.vendedor,
            status=self.status,
            usuario=self.user,
        )

    def crear_documento(self, cliente, numero, fecha):
        Documento.objects.create(
            numero=numero,
            cliente=cliente,
            fecha=fecha,
            vencimiento=fecha,
            monto=Decimal('100.00'),
            iva=self.iva,
            actualizado=timezone.make_aware(datetime.combine(fecha, datetime.min.time())),
            usuario=self.user,
            condicion=self.condicion,
        )

    def test_lists_clients_whose_latest_document_is_before_cutoff(self):
        fecha_corte = date(2025, 1, 1)
        cliente_atrasado = self.crear_cliente('Atrasado')
        self.crear_documento(cliente_atrasado, 'DOC-1', date(2024, 12, 31))

        cliente_limite = self.crear_cliente('En fecha límite')
        self.crear_documento(cliente_limite, 'DOC-2', fecha_corte)

        cliente_reciente = self.crear_cliente('Compra reciente')
        self.crear_documento(cliente_reciente, 'DOC-3', date(2024, 11, 1))
        self.crear_documento(cliente_reciente, 'DOC-4', date(2025, 1, 2))
        self.crear_cliente('Sin compras')

        response = self.client.post(
            reverse('clientes_sin_compra'),
            {'fecha_corte': fecha_corte.isoformat()},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            [cliente['nombre'] for cliente in response.context['xClientes']],
            ['Atrasado'],
        )
        self.assertEqual(response.context['xClientes'][0]['dias_sin_compra'], 1)

    def test_rejects_invalid_cutoff_date(self):
        response = self.client.post(
            reverse('clientes_sin_compra'),
            {'fecha_corte': 'fecha inválida'},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context['xError'],
            'Ingrese una fecha válida para consultar.',
        )

    def test_defaults_to_all_sellers(self):
        response = self.client.get(reverse('clientes_sin_compra'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['xVendedor_seleccionado'], 0)
        self.assertContains(response, '<option value="0" selected>TODOS</option>')
        self.assertTemplateUsed(response, 'app_gestion/base_m1.html')

    def test_combines_seller_and_latest_purchase_filters(self):
        otro_vendedor = Vendedor.objects.create(
            cedula='654321', nombre='Otro vendedor', ciudad=self.vendedor.ciudad,
            status=self.status, usuario=self.user,
        )
        cliente = self.crear_cliente('Seleccionado')
        self.crear_documento(cliente, 'V-1', date(2024, 12, 31))
        otro_cliente = self.crear_cliente('Otro cliente')
        otro_cliente.vendedor = otro_vendedor
        otro_cliente.save()
        self.crear_documento(otro_cliente, 'V-2', date(2024, 12, 30))
        reciente = self.crear_cliente('Reciente')
        self.crear_documento(reciente, 'V-3', date(2024, 12, 1))
        self.crear_documento(reciente, 'V-4', date(2025, 1, 1))

        for vendedor_id, nombres in (
            (0, ['Otro cliente', 'Seleccionado']),
            (self.vendedor.id, ['Seleccionado']),
            (otro_vendedor.id, ['Otro cliente']),
        ):
            with self.subTest(vendedor=vendedor_id):
                response = self.client.post(reverse('clientes_sin_compra'), {
                    'fecha_corte': '2025-01-01', 'vendedor': str(vendedor_id),
                })
                self.assertEqual(
                    [c['nombre'] for c in response.context['xClientes']], nombres,
                )
                self.assertEqual(response.context['xVendedor_seleccionado'], vendedor_id)
                self.assertContains(response, 'paging: false')
                self.assertContains(response, 'Generar PDF')

    def test_rejects_invalid_seller(self):
        for vendedor in ('incorrecto', '-1', '999999999'):
            with self.subTest(vendedor=vendedor):
                response = self.client.post(reverse('clientes_sin_compra'), {
                    'fecha_corte': '2025-01-01', 'vendedor': vendedor,
                })
                self.assertEqual(response.context['xClientes'], [])
                self.assertContains(response, 'Seleccione un vendedor válido.')

    def test_m2_uses_its_base_menu_and_home_link(self):
        self.user.groups.add(Group.objects.create(name='m2'))
        response = self.client.get(reverse('clientes_sin_compra'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_gestion/base_m2.html')
        self.assertTemplateUsed(response, 'app_gestion/navbar-menu_m2.html')
        self.assertContains(response, f'href="{reverse("clientes_sin_compra")}"')
        self.assertEqual(response.context['xInicio'], 'inicio_m2')
