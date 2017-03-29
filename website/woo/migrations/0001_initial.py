# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-28 20:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplianceName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appliance', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_num', models.IntegerField(default=1, max_length=10)),
                ('comp', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('ND', 'Not Done'), ('D', 'Done')], default='ND', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Usage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use', models.IntegerField(default=0, max_length=10)),
                ('recordtime', models.DateTimeField()),
                ('app_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='woo.ApplianceName')),
            ],
        ),
    ]