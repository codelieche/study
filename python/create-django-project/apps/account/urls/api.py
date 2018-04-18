# -*- coding:utf-8 -*-
from django.urls import path

from account.views.account import TestView


urlpatterns = [
    # 前缀：/api/v1/account/
    path('test', TestView.as_view(), name="test"),
]
