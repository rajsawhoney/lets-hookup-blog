# Generated by Django 3.0.3 on 2020-05-27 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0006_auto_20200505_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.FileField(upload_to='ArticleAssets'),
        ),
    ]
