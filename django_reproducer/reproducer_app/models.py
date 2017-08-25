# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from builtins import super

from django.db import models

class TestModel(models.Model):
    i = models.IntegerField()

    def save(self, **kwargs):
        self.i = 42
        super().save(**kwargs)
