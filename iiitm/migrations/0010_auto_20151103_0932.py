# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('iiitm', '0009_auto_20151103_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksissued',
            name='duedate',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 13, 9, 32, 58, 839625)),
        ),
        migrations.AlterField(
            model_name='booksissued',
            name='issuedate',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 3, 9, 32, 58, 839604)),
        ),
        migrations.AlterField(
            model_name='facultystatus',
            name='message',
            field=models.TextField(default=b'NOTHING'),
        ),
        migrations.AlterField(
            model_name='facultystatus',
            name='subject',
            field=models.CharField(default=b'None', max_length=50),
        ),
    ]
