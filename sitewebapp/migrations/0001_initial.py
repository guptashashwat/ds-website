# Generated by Django 3.0.6 on 2020-06-30 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('blog_text', models.TextField(max_length=50000)),
                ('image_url', models.URLField(blank=True, max_length=300, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Date created on.')),
                ('active', models.BooleanField(default=True)),
                ('author', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=255)),
                ('event_description', models.TextField(max_length=50000)),
                ('event_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Date of event : ')),
                ('event_mode', models.CharField(choices=[('1', 'Online'), ('2', 'Offline')], default='Online', max_length=15)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-event_datetime'],
            },
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('bio', models.TextField(blank=True, default='', null=True)),
                ('year', models.CharField(choices=[('1', 'Second'), ('2', 'Third'), ('3', 'Fourth')], default='Second', max_length=10)),
                ('post', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook_url', models.URLField(blank=True, max_length=300, null=True)),
                ('twitter_url', models.URLField(blank=True, max_length=300, null=True)),
                ('linkedin_url', models.URLField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_by', models.CharField(max_length=255, null=True)),
                ('comment', models.TextField(max_length=5000)),
                ('commented_on', models.DateTimeField(auto_now_add=True, verbose_name='Date commented on :')),
                ('active', models.BooleanField(default=True)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='sitewebapp.blog')),
            ],
            options={
                'ordering': ['-commented_on'],
            },
        ),
    ]
