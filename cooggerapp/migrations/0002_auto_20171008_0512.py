# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-08 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooggerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='iban',
            field=models.CharField(max_length=24, null=True, verbose_name='kart iban numarası'),
        ),
    ]
