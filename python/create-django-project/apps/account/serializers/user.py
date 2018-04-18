# -*- coding:utf-8 -*-
from rest_framework import serializers


class UserLoginSerializer(serializers.Serializer):
    """用户登录 Serializer"""
    username = serializers.CharField(max_length=40, required=True)
    password = serializers.CharField(max_length=40, required=True)

