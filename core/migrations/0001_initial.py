# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=240)),
                ('icon', models.CharField(max_length=240)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': '\u0418\u043d\u0444\u043e \u0411\u043b\u043e\u043a',
                'verbose_name_plural': '\u0418\u043d\u0444\u043e \u0411\u043b\u043e\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=240)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': '\u0423\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430',
                'verbose_name_plural': '\u0423\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0435 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b',
            },
        ),
    ]
