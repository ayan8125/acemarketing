# Generated by Django 3.2 on 2021-05-12 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_auto_20210505_2317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='_id',
            new_name='ID',
        ),
        migrations.RenameField(
            model_name='wallet',
            old_name='_id',
            new_name='ID',
        ),
    ]