# Generated by Django 4.0.3 on 2024-10-10 14:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestion', '0020_alter_documento_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='abonado',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10000.99)]),
            preserve_default=False,
        ),
    ]