# Generated by Django 3.0.3 on 2020-05-04 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0023_auto_20200503_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='testapp.Article', verbose_name='article_content'),
        ),
    ]
