# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-16 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_recipe_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
