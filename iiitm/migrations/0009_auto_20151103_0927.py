# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('iiitm', '0008_auto_20151103_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('subject', models.CharField(max_length=50)),
                ('status', models.CharField(default=b'NOT CONFIRM', max_length=50, choices=[(b'AVAILABLE', b'AVAILABLE'), (b'NOT AVAILABLE', b'NOT AVAILABLE'), (b'NOT CONFIRM', b'NOT CONFIRM')])),
                ('message', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='booksissued',
            name='duedate',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 13, 9, 27, 44, 428710)),
        ),
        migrations.AlterField(
            model_name='booksissued',
            name='issuedate',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 3, 9, 27, 44, 428685)),
        ),
    ]
