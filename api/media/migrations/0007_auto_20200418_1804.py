# Generated by Django 3.0.5 on 2020-04-18 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0006_auto_20200418_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='duration',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='media',
            name='mediaType',
            field=models.CharField(default='', max_length=128),
        ),
    ]
