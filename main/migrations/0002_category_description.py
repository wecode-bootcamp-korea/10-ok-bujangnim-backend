# Generated by Django 3.0.8 on 2020-07-27 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
