# Generated by Django 3.0.2 on 2020-01-31 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testapp', '0003_auto_20200131_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writer',
            name='fullname',
            field=models.OneToOneField(
                blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
