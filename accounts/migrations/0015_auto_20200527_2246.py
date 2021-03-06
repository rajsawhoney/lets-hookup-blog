# Generated by Django 3.0.3 on 2020-05-27 17:01

import accounts.models
from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20200527_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='profile_pic',
            field=models.ImageField(blank=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to=accounts.models.set_profile_Image_name, verbose_name='profile photo'),
        ),
    ]
