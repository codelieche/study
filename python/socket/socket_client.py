# -*- coding:utf-8 -*-
"""
Socket的客户端

每台机子【虚拟机/业务那边电脑】，都只能启动一个与服务端的连接。
当收到close的消息的时候，将断开客户端的连接

收到不同的消息做不同的操作。
"""
import socket
import time
import threading
import random


def recv_server_msg(client):
    """
    接收服务端的消息
    """
    # 接收服务端发来的消息
    while True:
        data = client.recv(1024)
        data = str(data, encoding="utf-8")

        time_now = time.strftime('%Y-%m-%d %H:%M:%S')
        print("{}\t收到消息：{}".format(time_now, data))

        if not data:
            break

        if data == 'close':
            client.close()
            time_now = time.strftime('%Y-%m-%d %H:%M:%S')
            print("{}\t已经关闭".format(time_now))
            break


def send_msg_to_server(client):
    """
    发送消息给服务端
    """
    try:
        for i in range(10):
            time.sleep(random.randint(1, 5))
            time_now = time.strftime('%Y%m%d%H%M%S')
            message = '消息{}'.format(time_now)

            message = bytes(message, encoding="utf-8")
            client.send(message)

        time_now = time.strftime('%Y-%m-%d %H:%M:%S')
        print("{}\t发送10次测试消息完毕，发送close".format(time_now))
        time.sleep(2.5)
        client.send(b'close me')
    except Exception as e:
        time_now = time.strftime('%Y-%m-%d %H:%M:%S')
        print('{}\t出现异常：{}'.format(time_now, str(e)))


def main():
    """
    客户端主程序
    """
    # 创建socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接服务器
    server_address = ('127.0.0.1', 9000)

    client.connect(server_address)

    # 启动个发送10次消息的线程
    t_msg = threading.Thread(target=send_msg_to_server, args=(client,))
    t_msg.start()

    # 启动接收数据的线程
    t = threading.Thread(target=recv_server_msg, args=(client,))

    t.start()
    t.join()


if __name__ == "__main__":
    # 开始执行
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    print("{}\t开始运行客户端".format(now))
    main()
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    print("{}\tDone".format(now))
