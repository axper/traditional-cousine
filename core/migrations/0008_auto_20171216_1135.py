# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-16 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20171216_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='short_description',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(default='Description Placeholder'),
        ),
    ]
