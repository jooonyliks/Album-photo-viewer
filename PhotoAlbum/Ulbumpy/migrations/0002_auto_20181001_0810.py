# Generated by Django 2.0.2 on 2018-10-01 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ulbumpy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='Description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='photos',
            name='ImagePhoto',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='photos',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
