from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestion', '0118_pago_ajuste'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='monto_iva',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Monto IVA'),
        ),
    ]
