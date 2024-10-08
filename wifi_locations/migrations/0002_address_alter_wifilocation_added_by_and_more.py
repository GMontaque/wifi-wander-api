# Generated by Django 5.1 on 2024-08-15 17:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wifi_locations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
                ('postcode', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='wifilocation',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wifi_location', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='wifilocation',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='wifi_locations.address'),
        ),
    ]
