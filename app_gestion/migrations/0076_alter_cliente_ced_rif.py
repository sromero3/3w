# Generated by Django 4.0.3 on 2024-11-13 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestion', '0075_vendedor_ciudad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='ced_rif',
            field=models.CharField(max_length=10),
        ),
    ]