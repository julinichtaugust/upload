# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-07-04 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('double_auction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ask',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=25),
        ),
        migrations.AlterField(
            model_name='bid',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=25),
        ),
        migrations.AlterField(
            model_name='contract',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=25),
        ),
    ]
