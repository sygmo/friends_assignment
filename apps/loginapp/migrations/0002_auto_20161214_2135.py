# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=45),
        ),
    ]
