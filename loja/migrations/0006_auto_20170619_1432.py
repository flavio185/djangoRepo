# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0005_auto_20170619_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roupas',
            name='imagem2',
            field=models.FileField(blank=True, upload_to='imagens_roupas'),
        ),
    ]
