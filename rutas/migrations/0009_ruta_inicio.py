# Generated by Django 4.2.4 on 2023-10-06 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rutas', '0008_ruta_alt_max_ruta_alt_min_ruta_desnivel_neg_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruta',
            name='inicio',
            field=models.CharField(default='null', max_length=150),
        ),
    ]
