# Generated by Django 4.0.3 on 2024-11-17 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestion', '0083_alter_cliente_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vendedor',
            options={'ordering': ['nombre'], 'verbose_name': 'Vendedor', 'verbose_name_plural': 'Vendedores'},
        ),
    ]
