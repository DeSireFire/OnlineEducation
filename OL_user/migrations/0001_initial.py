# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('User_email', models.CharField(max_length=100, unique=True)),
                ('User_name', models.CharField(max_length=20, unique=True)),
                ('User_pwd', models.CharField(max_length=40)),
                ('User_permission', models.CharField(max_length=20, default='3')),
                ('User_role', models.CharField(max_length=20)),
                ('User_info', models.CharField(max_length=20, default='')),
                ('User_address', models.CharField(max_length=100, default='')),
                ('User_phone', models.CharField(max_length=11, default='')),
            ],
        ),
    ]
