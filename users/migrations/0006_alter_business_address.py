# Generated by Django 3.2 on 2021-04-26 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_business'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
