# Generated by Django 4.0.3 on 2024-10-30 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestion', '0053_delete_asiento'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documento',
            options={'ordering': ['vencimiento', 'id'], 'verbose_name': 'Documento', 'verbose_name_plural': 'Documentos'},
        ),
    ]