# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import HttpResponse
from django.shortcuts import render
from mixer.backend.django import mixer

from reproducer_app.models import Post


def index(request):
    mixer.blend(Post, pk=42)
    return HttpResponse('Hello world!')
