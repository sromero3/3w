# Generated by Django 4.0.3 on 2024-11-21 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestion', '0094_excedente'),
    ]

    operations = [
        migrations.AddField(
            model_name='excedente',
            name='cli',
            field=models.ForeignKey(default=24, on_delete=django.db.models.deletion.CASCADE, to='app_gestion.cliente'),
            preserve_default=False,
        ),
    ]