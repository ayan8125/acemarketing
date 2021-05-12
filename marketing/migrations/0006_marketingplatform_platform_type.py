# Generated by Django 3.2 on 2021-04-28 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0005_marketingplatform_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketingplatform',
            name='platform_type',
            field=models.IntegerField(choices=[(0, 'Serch Engine'), (1, 'SocialMedia')], default=1),
        ),
    ]