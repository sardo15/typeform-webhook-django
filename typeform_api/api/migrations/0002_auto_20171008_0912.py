# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 09:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='typeform',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.TypeformForms'),
        ),
        migrations.AddField(
            model_name='typeformforms',
            name='questions',
            field=models.ManyToManyField(blank=True, to='api.TypeformQuestions'),
        ),
    ]