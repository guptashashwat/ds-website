# Generated by Django 3.0.7 on 2020-07-01 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitewebapp', '0002_auto_20200630_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='eventPosters/'),
        ),
        migrations.AddField(
            model_name='members',
            name='dp',
            field=models.ImageField(blank=True, null=True, upload_to='memberDPs/'),
        ),
    ]
