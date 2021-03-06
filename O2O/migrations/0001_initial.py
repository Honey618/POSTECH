# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 16:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaddate', models.DateTimeField(default=django.utils.timezone.now)),
                ('eventname', models.CharField(max_length=50)),
                ('eventdate', models.DateTimeField(blank=True, null=True)),
                ('eventtext', models.TextField()),
                ('file', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='poster',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posters', to='O2O.User'),
        ),
    ]
