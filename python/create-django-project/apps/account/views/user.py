# -*- coding:utf-8 -*-
"""
账号登陆登出相关api
"""
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from account.serializers.user import UserLoginSerializer


class LoginView(APIView):
    """
    用户登陆api View
    1. GET: 判断用户是否登陆
    2. POST: 账号登陆
    """

    def get(self, request):
        # get判断当前客户端是否登陆
        # 如果登陆了返回{logined: true},未登录返回{logined: false}
        user = request.user
        if user.is_authenticated:
            content = {
                "logined": True,
                "username": user.username,
                # "is_superuser": user.is_superuser
            }
        else:
            content = {
                "logined": False
            }

        return JsonResponse(data=content)

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data.get("username", "")
            password = serializer.validated_data.get("password", "")

            # 调用authenticate方法：注意settings.py中的AUTHTICATION_BACKENDS
            user = authenticate(username=username, password=password)

            if user is not None:
                # 登陆
                login(request, user)
                content = {
                    "status": True,
                    "username": user.username,
                    "message": "登陆成功",
                }
                return JsonResponse(data=content, status=status.HTTP_200_OK)
            else:
                content = {
                    "status": False,
                    "message": "账号或者密码不正确"
                }
                return JsonResponse(data=content, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def account_logout(request):
    """
    退出登陆
    :param request: http请求
    :return:
    """
    logout(request)
    # 有时候会传next
    next_url = request.GET.get("next", "/")
    return JsonResponse({"status": True, "next": next_url})
