# Generated by Django 4.0.3 on 2024-10-21 19:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestion', '0034_alter_documento_monto_alter_pago_monto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='monto',
            field=models.DecimalField(decimal_places=2, max_digits=9, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000000.99)]),
        ),
        migrations.AlterField(
            model_name='pago',
            name='forma',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_gestion.pagoforma'),
            preserve_default=False,
        ),
    ]
