# Generated by Django 2.2.15 on 2021-01-29 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitewebapp', '0011_auto_20210130_0150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auditionrounds',
            name='candidate',
        ),
        migrations.AddField(
            model_name='auditionrounds',
            name='candidate',
            field=models.ManyToManyField(related_name='candidates', to='sitewebapp.Candidates'),
        ),
    ]
