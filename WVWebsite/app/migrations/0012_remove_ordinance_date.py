# Generated by Django 3.0.5 on 2020-04-20 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_ordinance_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordinance',
            name='date',
        ),
    ]
