# Generated by Django 3.0.3 on 2020-05-06 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likecomment', '0011_comment_clapped'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='clapped',
            field=models.IntegerField(blank=True, null=True, verbose_name='Clapped Counts'),
        ),
    ]
