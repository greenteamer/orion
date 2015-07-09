# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_page_block_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='footer_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='footer_text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
