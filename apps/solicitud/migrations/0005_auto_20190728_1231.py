# Generated by Django 2.2.1 on 2019-07-28 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solicitud', '0004_auto_20190728_0420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='solicitud', to='solicitud.Eventos'),
        ),
    ]
