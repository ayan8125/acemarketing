# Generated by Django 3.2 on 2021-04-26 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210426_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True, verbose_name='staff status'),
        ),
    ]
