# Generated by Django 3.1.7 on 2021-04-16 12:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='last_activity',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='last activity'),
        ),
    ]
