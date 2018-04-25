# -*- coding:utf-8 -*-
from django.urls import path

from tags.views.tagvalue import TagValueListApiView

urlpatterns = [
    # 前缀：/api/v1/tags/tagvalue/
    path('list', TagValueListApiView.as_view(), name="list")
]
