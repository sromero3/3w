# Generated by Django 4.0.3 on 2024-10-10 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestion', '0019_alter_documento_iva_alter_iva_iva'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documento',
            options={'ordering': ['-vencimiento'], 'verbose_name': 'Documento', 'verbose_name_plural': 'Documentos'},
        ),
    ]
