# Generated by Django 4.0.3 on 2025-04-22 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestion', '0104_periodo'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodo',
            name='ano',
            field=models.CharField(default=2025, max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='periodo',
            name='numero_semana',
            field=models.CharField(max_length=2, unique=True),
        ),
    ]
