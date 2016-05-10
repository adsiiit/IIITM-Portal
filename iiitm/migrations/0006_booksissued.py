# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('iiitm', '0005_auto_20151031_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooksIssued',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('unitid', models.CharField(max_length=128)),
                ('issuedate', models.DateTimeField(default=datetime.datetime(2015, 10, 31, 18, 20, 34, 227040))),
                ('duedate', models.DateTimeField(default=datetime.datetime(2015, 11, 10, 18, 20, 34, 227065))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
