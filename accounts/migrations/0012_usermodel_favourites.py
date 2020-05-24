# Generated by Django 3.0.3 on 2020-05-15 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0037_auto_20200514_0036'),
        ('accounts', '0011_ipaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='favourites',
            field=models.ManyToManyField(related_name='fav_articles', to='testapp.Article', verbose_name='Favourite Articles'),
        ),
    ]
