# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-25 10:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0051_auto_20210222_1452'),
        ('core', '0050_xslt_1-3-10'),
        ('journal', '0041_issue_short_description'),
        ('imports', '0002_auto_20190829_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExportFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submission.Article')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.File')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.Journal')),
            ],
        ),
    ]
