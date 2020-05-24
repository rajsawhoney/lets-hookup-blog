# Generated by Django 3.0.3 on 2020-05-08 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200506_1504'),
        ('testapp', '0030_auto_20200507_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='followed_by',
            field=models.ManyToManyField(blank=True, null=True, related_name='followers', to='accounts.UserModel', verbose_name='Followed by'),
        ),
    ]
