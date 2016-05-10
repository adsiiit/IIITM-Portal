# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20151030_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(default=b'N', max_length=2, choices=[(b'N', b'SELECT'), (b'M', b'Male'), (b'F', b'Female')]),
        ),
    ]
