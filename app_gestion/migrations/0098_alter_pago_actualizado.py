# Generated by Django 4.0.3 on 2024-12-09 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestion', '0097_pago_track'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='actualizado',
            field=models.DateTimeField(),
        ),
    ]
