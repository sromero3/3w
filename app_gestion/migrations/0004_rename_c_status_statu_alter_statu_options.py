# Generated by Django 4.0.3 on 2024-10-08 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestion', '0003_cliente_observacion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='C_status',
            new_name='Statu',
        ),
        migrations.AlterModelOptions(
            name='statu',
            options={'ordering': ['id'], 'verbose_name': 'Statu', 'verbose_name_plural': 'Status'},
        ),
    ]