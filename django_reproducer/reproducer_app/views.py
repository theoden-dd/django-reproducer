# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Hello world!')
