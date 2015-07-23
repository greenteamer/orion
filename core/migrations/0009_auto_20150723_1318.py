# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_contacts_social'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialContacts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0439 \u0441\u0435\u0442\u0438')),
                ('link', models.CharField(max_length=150, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u044c\u043d\u0443\u044e \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443')),
            ],
            options={
                'verbose_name': '\u0421\u043b\u0446\u0438\u0430\u043b\u044c\u043d\u0430\u044f \u0441\u0435\u0442\u044c',
                'verbose_name_plural': '\u0421\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0435 \u0441\u0435\u0442\u0438',
            },
        ),
        migrations.DeleteModel(
            name='Social',
        ),
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name': '\u041a\u043e\u043d\u0442\u0430\u043a\u0442 \u0441\u0430\u0439\u0442\u0430', 'verbose_name_plural': '\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b \u0441\u0430\u0439\u0442\u0430'},
        ),
        migrations.AlterField(
            model_name='contacts',
            name='name',
            field=models.CharField(max_length=20, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d'),
        ),
        migrations.AddField(
            model_name='socialcontacts',
            name='contact',
            field=models.ForeignKey(to='core.Contacts'),
        ),
    ]
