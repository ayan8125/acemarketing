# Generated by Django 3.2 on 2021-05-04 15:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_alter_business_postcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('goal', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.business')),
            ],
        ),
    ]
