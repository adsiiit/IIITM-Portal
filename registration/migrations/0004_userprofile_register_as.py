# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20151030_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='register_as',
            field=models.CharField(default=b'OR', max_length=2, choices=[(b'FY', b'FACULTY'), (b'ST', b'STUDENT'), (b'SF', b'STAFF'), (b'OR', b'OTHER')]),
            preserve_default=True,
        ),
    ]
