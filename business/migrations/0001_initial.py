# Generated by Django 3.2 on 2021-05-03 09:51

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
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='business', max_length=255, null=True)),
                ('runs_online', models.BooleanField(default=False)),
                ('runs_locally', models.BooleanField(default=False)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.IntegerField(blank=True, choices=[(0, 'England'), (1, 'Scotland'), (2, 'Wales'), (4, 'Northern Irealand')], default=0, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('zipcode', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessUSP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.business')),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.sector'),
        ),
        migrations.AddField(
            model_name='business',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
