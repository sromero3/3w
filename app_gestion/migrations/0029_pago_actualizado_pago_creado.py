# Generated by Django 4.0.3 on 2024-10-15 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestion', '0028_rename_descripcion_pago_observacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='actualizado',
            field=models.DateTimeField(auto_now_add=True, default='2024-10-15 14:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pago',
            name='creado',
            field=models.DateTimeField(auto_now_add=True, default='2024-10-15 14:00'),
            preserve_default=False,
        ),
    ]
