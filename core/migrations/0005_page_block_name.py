# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150709_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='block_name',
            field=models.CharField(default='', max_length=240),
            preserve_default=False,
        ),
    ]
