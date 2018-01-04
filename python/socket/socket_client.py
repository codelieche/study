# -*- coding:utf-8 -*-

import socket

# 创建个socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务端
client.connect(('127.0.0.1', 9000))

# 发送数据
client.send('Hello')
