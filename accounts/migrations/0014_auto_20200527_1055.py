# Generated by Django 3.0.3 on 2020-05-27 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20200517_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='about_me',
            field=models.TextField(blank=True, default='I am a good person! I am this and that', verbose_name='About me:'),
        ),
    ]