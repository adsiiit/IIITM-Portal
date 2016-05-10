# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iiitm', '0003_auto_20151031_0712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='user',
        ),
        migrations.AddField(
            model_name='complaint',
            name='username',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]
