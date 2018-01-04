# -*- coding:utf-8 -*-
import socket

# 创建一个socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
server.bind(('127.0.0.1', 9000))

# 捕获连接
server.listen(10)

while True:
    conn, address = server.accept()
    print("接收到新的连接：", conn, address)


