# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=100)


class Post(models.Model):
    content = models.CharField(max_length=140)
    tags = models.ManyToManyField(Tag, blank=True)
