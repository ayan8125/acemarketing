# Generated by Django 3.2 on 2021-05-12 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0008_alter_campaignroot_business'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaign',
            old_name='_id',
            new_name='ID',
        ),
        migrations.RenameField(
            model_name='campaignroot',
            old_name='_id',
            new_name='ID',
        ),
        migrations.RenameField(
            model_name='campaigntype',
            old_name='_id',
            new_name='ID',
        ),
        migrations.RenameField(
            model_name='marketingplatform',
            old_name='_id',
            new_name='ID',
        ),
    ]
