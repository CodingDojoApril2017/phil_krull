# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmailManager',
        ),
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.CharField(max_length=255),
        ),
    ]
