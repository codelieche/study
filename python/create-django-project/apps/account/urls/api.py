# -*- coding:utf-8 -*-
from django.urls import path, include

from account.views.user import LoginView, account_logout
from account.views.account import TestView

urlpatterns = [
    # 前缀：/api/v1/account/
    path('login', LoginView.as_view(), name="login"),
    path('logout', account_logout, name="logout"),

    # Account Group Api
    path('group/', include(arg=('account.urls.group', 'account'), namespace='group')),
    # Account User Api
    path('user/', include(arg=("account.urls.user", 'account'), namespace="user")),
    # 测试api
    path('test', TestView.as_view(), name="test"),
]
