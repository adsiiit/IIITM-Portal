# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('gender', models.CharField(default=b'None', max_length=2, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('age', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=1024)),
                ('contact', models.BigIntegerField(unique=True)),
                ('stream', models.CharField(default=b'NONE', max_length=6, choices=[(b'IPG', b'IPG'), (b'MTECH', b'MTECH'), (b'MBA', b'MBA'), (b'PHD', b'PHD'), (b'OTHER', b'OTHER'), (b'NONE', b'NONE')])),
                ('picture', models.ImageField(upload_to=b'profile_images/', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
