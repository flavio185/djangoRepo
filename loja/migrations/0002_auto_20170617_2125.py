# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roupas',
            name='genero',
            field=models.CharField(choices=[('Feminino', 'FEMININO'), ('Masculino', 'MASCULINO'), ('Unisex', 'UNISEX')], max_length=10),
        ),
    ]