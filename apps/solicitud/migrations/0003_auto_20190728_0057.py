# Generated by Django 2.2.1 on 2019-07-28 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitud', '0002_solicitud_extra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='extra',
            field=models.CharField(default=None, max_length=200),
        ),
    ]