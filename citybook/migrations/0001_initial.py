# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('name', models.CharField(max_length=255, unique=True, serialize=False, verbose_name='Name', primary_key=True)),
                ('food', models.CharField(max_length=255, verbose_name='Food')),
                ('timezone', models.CharField(max_length=6, verbose_name='Time Zone')),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
            bases=(models.Model,),
        ),
    ]
