# Generated by Django 4.0.3 on 2024-11-13 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestion', '0080_condicion_remove_documento_tipo_delete_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='condicion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_gestion.condicion'),
            preserve_default=False,
        ),
    ]