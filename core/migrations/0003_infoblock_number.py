# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_infoblock_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoblock',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
