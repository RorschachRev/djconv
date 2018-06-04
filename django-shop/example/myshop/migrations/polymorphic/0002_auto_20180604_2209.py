# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-04 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartcard',
            name='speed',
            field=models.CharField(choices=[('4', '4 MB/s'), ('20', '20 MB/s'), ('30', '30 MB/s'), ('40', '40 MB/s'), ('48', '48 MB/s'), ('80', '80 MB/s'), ('95', '95 MB/s'), ('280', '280 MB/s')], max_length=8, verbose_name='Transfer Speed'),
        ),
    ]