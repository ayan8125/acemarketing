# Generated by Django 3.2 on 2021-05-03 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_rename_businessusp_usp'),
        ('marketing', '0007_auto_20210503_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaignroot',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.business'),
        ),
    ]
