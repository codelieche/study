# -*- coding:utf-8 -*-
import socket
import threading
import time

client_dict = {}


def recv_client_message(conn, address):
    """
    Socket客户端
    :param conn: 客户端连接socket
    :param address: 客户端的地址
    :return:
    """
    while True:
        data = conn.recv(1024)
        print(address, "Get Message:", data)
        time.sleep(10)
        conn.send('Server Recv You Message')


def accept_client(server):
    """
    Socket服务端
    :param server:
    :return:
    """
    while True:
        conn, address = server.accept()
        client_dict[address[0]] = conn
        # 输出信息
        print('New Client:', address)
        t = threading.Thread(target=recv_client_message, args=(conn, address))
        t.start()


def test_msg(server):
    time.sleep(10)
    server

# 创建一个socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
server.bind(('127.0.0.1', 9000))

# 捕获连接
server.listen(10)

while True:
    conn, address = server.accept()
    print("New Client：", address)
    client_dict[address[0]] = conn
    t = threading.Thread(target=recv_client_message, args=(conn, address))
    t.start()

# 启动监听连接的线程
# t_accept = threading.Thread(target=accept_client, args=(server,))
# t_accept.start()

#





