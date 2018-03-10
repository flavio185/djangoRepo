# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 19:08
from __future__ import unicode_literals

from django.db import migrations, models
import loja.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roupas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(default=loja.models.auto_increment_roupa_id, max_length=10)),
                ('nome', models.CharField(max_length=70)),
                ('tipo', models.CharField(max_length=70)),
                ('genero', models.CharField(choices=[('feminino', 'FEMININO'), ('masculino', 'MASCULINO'), ('unisex', 'UNISEX')], max_length=10)),
                ('data_inclusao', models.DateTimeField(blank=True, null=True)),
                ('tamanho', models.CharField(blank=True, max_length=10, null=True)),
                ('valor_pago', models.CharField(blank=True, max_length=8, null=True)),
                ('valor_venda', models.CharField(blank=True, max_length=8, null=True)),
                ('estoque', models.IntegerField(blank=True, default=1, null=True)),
                ('imagem', models.ImageField(blank=True, upload_to='imagens_roupas')),
                ('imagem1', models.ImageField(blank=True, upload_to='imagens_roupas')),
                ('imagem2', models.ImageField(blank=True, upload_to='imagens_roupas')),
            ],
        ),
    ]
