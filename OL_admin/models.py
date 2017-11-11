# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    pwd = models.CharField(max_length=50)
    limits = models.CharField(max_length=10,default='normal')
    isDelte = models.BooleanField(default=False)
    def __str__(self):
        return self.username

