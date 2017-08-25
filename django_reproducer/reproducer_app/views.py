# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import HttpResponse
from django.shortcuts import render

from django_reproducer.serializers import PostSerializer
from reproducer_app.models import Post, Tag


def index(request):
    p = Post.objects.create(content='Cool!')
    p.tags.set([Tag.objects.create(title='tag1'), Tag.objects.create(title='tag2')])
    s = PostSerializer(p)
    print(s.data)
    return HttpResponse('Hello world!')
