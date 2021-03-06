# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='mode',
            field=models.CharField(choices=[('&status=completed', 'Completed'), ('&status=current', 'Currently watching'), ('&status=planned', 'Plan to watch'), ('&status=completed', 'On hold'), ('&status=dropped', 'droped')], default='&status=completed', max_length=25),
        ),
    ]
