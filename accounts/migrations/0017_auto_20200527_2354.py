# Generated by Django 3.0.3 on 2020-05-27 18:09

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20200527_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='profile_pic',
            field=models.FileField(blank=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='user_profile_pic', verbose_name='profile photo'),
        ),
    ]