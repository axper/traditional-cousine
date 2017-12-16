# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-16 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20171216_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='step',
            name='time',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='step',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterUniqueTogether(
            name='step',
            unique_together=set([('order', 'recipe')]),
        ),
    ]