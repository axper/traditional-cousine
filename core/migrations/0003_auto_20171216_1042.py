# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-16 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171216_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(default='Description Placeholder', max_length=20000),
        ),
    ]
