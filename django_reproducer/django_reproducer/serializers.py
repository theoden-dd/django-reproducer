# coding: utf-8
from __future__ import (
    absolute_import, division, print_function, unicode_literals,
)

from django.core.validators import MaxLengthValidator
from rest_framework import serializers

from reproducer_app.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        extra_kwargs = {
            'tags': {'validators': [MaxLengthValidator(1)]}
        }
        fields = '__all__'
