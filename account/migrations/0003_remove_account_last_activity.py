# Generated by Django 3.1.7 on 2021-04-16 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_account_last_activity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='last_activity',
        ),
    ]
