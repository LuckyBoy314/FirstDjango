# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-05 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='板块名称')),
                ('desc', models.CharField(max_length=36, verbose_name='板块描述')),
                ('manager_name', models.CharField(max_length=12, verbose_name='板块管理员')),
                ('status', models.IntegerField(choices=[(0, '正常'), (-1, '不正常')], default=0, verbose_name='状态')),
            ],
        ),
    ]