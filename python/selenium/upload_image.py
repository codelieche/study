# -*- coding:utf-8 -*-
import sys

import requests


def upload_image_to_web(filename, imagedata):
    """
    上传图片到web后台
    这样可以让browser直接get_screenshot_as_png然后发送到后台
    :param filename: 文件名
    :param imagedata: 图片数据
    :return:
    """
    # 1. 先实例化Session类
    session = requests.Session()

    # 2. 先登录
    login_url = 'http://127.0.0.1:8080/api/1.0/account/login'
    data = {
        "username": 'user_name',
        "password": "pwd"
    }
    response = session.post(url=login_url, data=data)
    if response.ok:
        result = response.json()
        print(result)
    else:
        print("登陆失败")
        sys.exit(1)

    # 3. 上传图片
    upload_url = "http://127.0.0.1:8080/api/1.0/cmdb/document/upload"

    data = {
        "filename": filename,
    }

    files = {
        # "file": open('./test.png', 'rb')
        "file": imagedata
    }

    response = session.post(url=upload_url, data=data, files=files)

    if response.ok:
        result = response.json()
        print(result)
    else:
        print("上传图片失败")
