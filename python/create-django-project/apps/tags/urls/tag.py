# -*- coding:utf-8 -*-
from django.urls import path

from tags.views.tag import (
    TagCreateApiView,
    TagListApiView,
    TagDetailApiView
)

urlpatterns = [
    # 前缀：/api/v1/tags/tag/
    path('create', TagCreateApiView.as_view(), name="create"),
    path('list', TagListApiView.as_view(), name="list"),
    path('<int:pk>', TagDetailApiView.as_view(), name="detail"),
    path('<str:tag>', TagDetailApiView.as_view(lookup_field="tag"), name="detail2"),
]
