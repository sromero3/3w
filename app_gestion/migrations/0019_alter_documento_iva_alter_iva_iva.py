# Generated by Django 4.0.3 on 2024-10-10 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestion', '0018_iva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='iva',
            field=models.ForeignKey(default='Pendiente', on_delete=django.db.models.deletion.CASCADE, to='app_gestion.iva'),
        ),
        migrations.AlterField(
            model_name='iva',
            name='iva',
            field=models.CharField(max_length=10),
        ),
    ]