# Generated by Django 3.0.7 on 2020-07-28 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_auto_20200726_0015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subtitle',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('subscription', models.CharField(max_length=500)),
                ('number', models.CharField(max_length=100)),
                ('cate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.Category')),
                ('is_activated', models.CharField(blank=True, default='Y', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'subtitle',
            },
        ),
    ]
