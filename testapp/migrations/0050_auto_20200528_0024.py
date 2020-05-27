# Generated by Django 3.0.3 on 2020-05-27 18:39

from django.db import migrations, models
import gdstorage.storage
import testapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0049_auto_20200527_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.FileField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to=testapp.models.set_thumbnail_name, verbose_name='Thumbnail'),
        ),
    ]
