# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-09 08:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_auto_20181109_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Goodsdetail'),
        ),
    ]
