# Generated by Django 3.0.7 on 2020-10-02 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TagType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('type_of', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='media.TagType')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('tz', models.CharField(max_length=4)),
                ('title', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=255)),
                ('full_title', models.CharField(blank=True, max_length=255)),
                ('url', models.URLField(blank=True, default=None)),
                ('format', models.CharField(max_length=5)),
                ('jump', models.IntegerField(default=0)),
                ('trim', models.IntegerField(default=0)),
                ('volume', models.DecimalField(decimal_places=2, default=1.0, max_digits=5)),
                ('mute', models.BooleanField(default=False)),
                ('content', models.TextField(blank=True, default='')),
                ('image', models.URLField(blank=True, default='')),
                ('image_caption', models.TextField(blank=True, default='')),
                ('approved', models.BooleanField(default=False)),
                ('collection', models.ManyToManyField(blank=True, to='media.Collection')),
                ('tags', models.ManyToManyField(blank=True, to='media.Tag')),
            ],
            options={
                'verbose_name': 'media',
                'verbose_name_plural': 'media items',
                'ordering': ['start_date'],
            },
        ),
        migrations.AddField(
            model_name='collection',
            name='type_of',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='media.TagType'),
        ),
    ]
