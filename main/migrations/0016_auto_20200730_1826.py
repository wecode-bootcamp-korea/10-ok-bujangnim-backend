# Generated by Django 3.0.8 on 2020-07-30 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20200730_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='is_activated',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='is_activated',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
