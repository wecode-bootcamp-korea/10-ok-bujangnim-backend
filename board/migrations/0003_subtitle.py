# Generated by Django 3.0.7 on 2020-07-25 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20200725_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subtitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subscrition', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=30)),
            ],
        ),
    ]