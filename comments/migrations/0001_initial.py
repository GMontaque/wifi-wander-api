# Generated by Django 5.1 on 2024-08-17 09:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wifi_locations', '0002_address_alter_wifilocation_added_by_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wifi_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wifi_locations.wifilocation')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
