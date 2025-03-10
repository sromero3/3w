# Generated by Django 4.0.3 on 2024-11-20 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_gestion', '0093_vendedor_actualizado_vendedor_creado_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Excedente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concepto', models.CharField(blank=True, max_length=50, null=True)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=9)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=9)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now_add=True)),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_gestion.documento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
