# Generated by Django 4.0.3 on 2024-10-23 15:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestion', '0039_alter_pago_monto_alter_pago_monto_procesar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='monto',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(999999.99)]),
        ),
    ]
