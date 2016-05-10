# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=128)),
                ('type_of_complaint', models.CharField(default=b'OT', max_length=2, choices=[(b'AC', b'Academics'), (b'AT', b'Accounts'), (b'AD', b'Administration'), (b'HO', b'Hostel'), (b'HP', b'Hospital'), (b'LI', b'Library'), (b'MI', b'Missing'), (b'OT', b'Others')])),
                ('complaint_subject', models.CharField(max_length=200)),
                ('complaint_desc', models.TextField()),
                ('solved', models.CharField(default=b'NOT SOLVED', max_length=50, choices=[(b'SOLVED', b'solved'), (b'NOT SOLVED', b'unsolved'), (b'UNDER CONSIDERATION', b'under consideration')])),
                ('comment', models.TextField()),
                ('preference', models.IntegerField(default=0, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
