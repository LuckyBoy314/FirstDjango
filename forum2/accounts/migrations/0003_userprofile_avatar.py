# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-07-25 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.CharField(blank=True, max_length=300, verbose_name='头像'),
        ),
    ]
