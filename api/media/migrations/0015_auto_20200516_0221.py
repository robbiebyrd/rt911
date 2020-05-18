# Generated by Django 3.0.6 on 2020-05-16 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0014_media_trim'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='media',
            name='tags',
            field=models.ManyToManyField(to='media.Tag'),
        ),
    ]
