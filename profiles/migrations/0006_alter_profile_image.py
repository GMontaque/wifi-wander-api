# Generated by Django 5.1 on 2024-08-24 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_profile_memorable_word'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default_profile_q35ywj', null=True, upload_to='images/'),
        ),
    ]
