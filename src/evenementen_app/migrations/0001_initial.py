# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 14:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=256)),
                ('url_title', models.CharField(max_length=256)),
                ('image', models.ImageField(blank=True, upload_to='/media/evenement/')),
                ('tijdstip', models.DateTimeField()),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Evenementen',
                'ordering': ['-tijdstip'],
                'verbose_name': 'Evenement',
            },
        ),
        migrations.CreateModel(
            name='Inschrijving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('voornaam', models.CharField(max_length=64)),
                ('achternaam', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('telefoon', models.CharField(max_length=64)),
                ('bericht', models.TextField()),
                ('evenement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evenementen_app.Evenement')),
            ],
            options={
                'verbose_name_plural': 'Inschrijvingen',
                'ordering': ['-timestamp'],
                'verbose_name': 'Inschrijving',
            },
        ),
    ]