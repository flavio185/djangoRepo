# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_auto_20170619_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roupas',
            name='valor_pago',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='roupas',
            name='valor_venda',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
