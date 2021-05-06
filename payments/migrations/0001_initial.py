# Generated by Django 3.2 on 2021-05-03 23:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('currency', models.CharField(default='Pound sterling', max_length=255)),
                ('balanceamt', models.FloatField(default=0.0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('_id', models.CharField(auto_created=True, max_length=255, primary_key=True, serialize=False)),
                ('amount', models.FloatField(default=0.0)),
                ('status', models.IntegerField(choices=[(0, 'Initiaited'), (1, 'Pending'), (2, 'Completed'), (3, 'Failed')], default=0)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=255, null=True)),
                ('razorpay_order_id', models.CharField(blank=True, max_length=255, null=True)),
                ('razorpay_signature', models.CharField(blank=True, max_length=255, null=True)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.wallet')),
            ],
        ),
    ]
