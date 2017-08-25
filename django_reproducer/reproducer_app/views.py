# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import HttpResponse
from django.shortcuts import render

from reproducer_app.models import TestModel


def index(request):
    tm = TestModel(i=5)
    tm.save()
    return HttpResponse('Hello world!')
