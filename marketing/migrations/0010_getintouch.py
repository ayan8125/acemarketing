# Generated by Django 3.2 on 2021-05-19 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0009_auto_20210512_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='GetInTouch',
            fields=[
                ('ID', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('email', models.EmailField(default='your@email.com', max_length=254)),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Proccessing'), (2, 'Resolved')], default=0)),
            ],
        ),
    ]
