# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-28 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20170228_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='logo_link',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
