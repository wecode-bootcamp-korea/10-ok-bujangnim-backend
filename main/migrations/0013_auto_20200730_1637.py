# Generated by Django 3.0.8 on 2020-07-30 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200727_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='is_activated',
            field=models.CharField(blank=True, default=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='category',
            name='is_activated',
            field=models.CharField(blank=True, default=True, max_length=10),
        ),
    ]
