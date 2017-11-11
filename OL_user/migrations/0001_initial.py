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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('User_email', models.CharField(unique=True, max_length=100)),
                ('User_name', models.CharField(unique=True, max_length=20)),
                ('User_pwd', models.CharField(max_length=50)),
                ('User_permission', models.CharField(default='3', max_length=20)),
                ('User_role', models.CharField(max_length=20)),
                ('User_info', models.CharField(default='', max_length=20)),
                ('User_address', models.CharField(default='', max_length=100)),
                ('User_phone', models.CharField(default='', max_length=11)),
            ],
        ),
    ]
