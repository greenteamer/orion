# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_infoblock_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='trigger1',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='trigger2',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
