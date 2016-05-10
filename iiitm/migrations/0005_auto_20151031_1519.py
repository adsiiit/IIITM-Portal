# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iiitm', '0004_auto_20151031_0743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('author', models.CharField(max_length=128)),
                ('bookid', models.CharField(max_length=128)),
                ('quantity', models.IntegerField(default=0)),
                ('available', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='solved',
            field=models.CharField(default=b'NOT SOLVED', max_length=50, choices=[(b'SOLVED', b'Solved'), (b'NOT SOLVED', b'Unsolved'), (b'UNDER CONSIDERATION', b'Under Consideration')]),
        ),
    ]
