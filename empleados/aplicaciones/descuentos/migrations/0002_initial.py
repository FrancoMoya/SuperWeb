# Generated by Django 4.2.5 on 2023-11-04 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('descuentos', '0001_initial'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cupon',
            name='usuarios_asociados',
            field=models.ManyToManyField(blank=True, to='usuario.user'),
        ),
    ]
