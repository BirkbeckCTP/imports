# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-04-26 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0006_auto_20220316_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='csvimportcreatearticle',
            name='file_id',
            field=models.CharField(blank=True, max_length=999, null=True),
        ),
    ]
