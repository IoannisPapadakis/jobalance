# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-19 10:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobTitle', models.TextField()),
                ('salary', models.CharField(blank=True, max_length=60, null=True)),
                ('relocation', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regionId', models.CharField(max_length=30)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('category', models.CharField(max_length=10)),
                ('etks', models.CharField(max_length=5)),
                ('active', models.BooleanField()),
                ('deleted', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='cv',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='where', to='api.Region'),
        ),
        migrations.AddField(
            model_name='cv',
            name='speciality',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='spec', to='api.Speciality'),
        ),
    ]