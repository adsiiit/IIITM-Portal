# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('iiitm', '0007_auto_20151031_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksissued',
            name='duedate',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 13, 8, 52, 32, 186031)),
        ),
        migrations.AlterField(
            model_name='booksissued',
            name='issuedate',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 3, 8, 52, 32, 186007)),
        ),
    ]
