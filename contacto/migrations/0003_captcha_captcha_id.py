# Generated by Django 4.2.4 on 2023-10-27 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0002_remove_captcha_captcha_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='captcha',
            name='captcha_id',
            field=models.CharField(default='0', max_length=20, unique=True),
        ),
    ]
