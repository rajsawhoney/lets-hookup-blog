# Generated by Django 3.0.3 on 2020-05-17 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20200517_1409'),
        ('likecomment', '0014_auto_20200513_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_by', to='accounts.UserModel', verbose_name='UserName'),
        ),
    ]
