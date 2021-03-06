# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-09 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arch', '__first__'),
        ('operatingsystems', '__first__'),
        ('packages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Erratum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('etype', models.CharField(max_length=255)),
                ('issue_date', models.DateTimeField()),
                ('synopsis', models.CharField(max_length=255)),
                ('arches', models.ManyToManyField(blank=True, to='arch.MachineArchitecture')),
                ('packages', models.ManyToManyField(blank=True, to='packages.Package')),
            ],
        ),
        migrations.CreateModel(
            name='ErratumReference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='erratum',
            name='references',
            field=models.ManyToManyField(blank=True, to='packages.ErratumReference'),
        ),
        migrations.AddField(
            model_name='erratum',
            name='releases',
            field=models.ManyToManyField(blank=True, to='operatingsystems.OSGroup'),
        ),
    ]
