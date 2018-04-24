# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 01:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='idk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rte', models.PositiveSmallIntegerField(default=0)),
                ('street_name', models.CharField(max_length=200)),
                ('from_adress', models.IntegerField()),
                ('to_adress', models.IntegerField()),
                ('of_month', models.IntegerField()),
                ('meridian', models.BooleanField()),
                ('side', models.CharField(max_length=10)),
                ('from_street', models.CharField(max_length=200)),
                ('to_street', models.CharField(max_length=200)),
                ('optout', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Weekday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='idk',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sweeping.Weekday'),
        ),
    ]