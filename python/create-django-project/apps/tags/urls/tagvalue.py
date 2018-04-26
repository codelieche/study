# -*- coding:utf-8 -*-
from django.urls import path

from tags.views.tagvalue import TagValueListApiView
from tags.views.objecttag import ObjectTagValueListApiView

urlpatterns = [
    # 前缀：/api/v1/tags/tagvalue/
    path('list', TagValueListApiView.as_view(), name="list"),
    path('<str:app_label>/<str:model>/<int:object_id>',
         ObjectTagValueListApiView.as_view(lookup_field=("app_label", "model", "object_id")),
         name="object_tagvalue_list"),
]
