# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-28 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_university_logo_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='img/logos'),
        ),
    ]
