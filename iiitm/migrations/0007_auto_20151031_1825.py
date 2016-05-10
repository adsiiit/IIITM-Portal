# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('iiitm', '0006_booksissued'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksissued',
            name='username',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booksissued',
            name='duedate',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 10, 18, 25, 6, 10970)),
        ),
        migrations.AlterField(
            model_name='booksissued',
            name='issuedate',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 18, 25, 6, 10943)),
        ),
    ]
