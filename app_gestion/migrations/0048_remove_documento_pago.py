# Generated by Django 4.0.3 on 2024-10-23 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestion', '0047_documento_pago'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documento',
            name='pago',
        ),
    ]
