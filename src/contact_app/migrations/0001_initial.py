# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=32)),
                ('lastname', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('birthday', models.DateField(blank=True)),
                ('gender', models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male'), ('P', 'Prefer not to say')], max_length=1)),
                ('company', models.CharField(blank=True, max_length=64)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Contact Messeges',
                'verbose_name': 'Contact Message',
                'ordering': ['-timestamp'],
                'get_latest_by': 'timestamp',
            },
        ),
    ]