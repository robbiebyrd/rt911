# Generated by Django 3.0.5 on 2020-04-18 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0005_media_approved'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='media',
            options={'ordering': ['start_date'], 'verbose_name_plural': 'media'},
        ),
        migrations.AlterField(
            model_name='media',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='👍'),
        ),
    ]