# -*- coding:utf-8 -*-
"""
对象标签相关 serializer
"""
from rest_framework import serializers

from tags.models import Tag, TagValue, ObjectTag


class ObjectTagCreateSerializer(serializers.Serializer):
    """
    创建对象标签序列化Model
    """
    tag = serializers.CharField(max_length=40)
    value = serializers.CharField(max_length=40)
    app_label = serializers.CharField(max_length=40)
    model = serializers.CharField(max_length=40)
    object_id = serializers.IntegerField()


class ObjectTagModelSerializer(serializers.ModelSerializer):
    """
    ObjectTag Model Serializer
    """
    tag = serializers.CharField(source="tagvalue.tag.tag")
    value = serializers.CharField(source="tagvalue.value")

    class Meta:
        model = ObjectTag
        fields = ("id", "tag", "value", "app_label", "model", "object_id")
