# Generated by Django 4.0.3 on 2024-11-06 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestion', '0069_alter_cliente_ced_rif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendedor',
            name='cedula',
            field=models.CharField(max_length=9, unique=True),
        ),
    ]