# -*- coding:utf-8 -*-
"""
Socket服务端，只在一台服务器上运行，接收不同客户端的连接
每台host只能有一个客户端与服务端连接

"""
import socket
import time
import threading

# 我们根据客户端的ip，把连接对象加入到client_dict中
client_dict = {}


def recv_client_message(conn, address):
    """
    接收客户端的消息
    :param conn: 客户端连接socket
    :param address: 客户端的地址和端口号
    :return
    """
    flag = True
    while flag:
        # 接收客户端的消息，一般消息长度都是小于1024的
        try:
            data = conn.recv(1024)
            data = str(data, encoding="utf-8")
            print(address, "收到消息：", data)

            # 延时10秒后，返回消息内容给客户端
            if data == 'close me':
                msg = 'close'
                # 同时把循环的标志设置为False
                flag = False
            else:
                msg = "收到你的消息: {}".format(data)

            msg = bytes(msg, encoding="utf-8")
            conn.send(msg)
        except (ConnectionResetError, BrokenPipeError, OSError) as e:
            time_now = time.strftime('%Y-%m-%d %H:%M:%S')
            print('{}\t出现异常：{}'.format(time_now, str(e)))
            # 出现异常 就断开这个链接
            flag = False
            break
    time_now = time.strftime('%Y-%m-%d %H:%M:%S')
    print('{}\t监听客户端({})的线程执行完毕！'.format(time_now, id(conn)))


def close_client_connect(conn):
    """
    关闭客户端的链接
    """
    try:
        conn.send(b'close')
        print("发送关闭客户端消息成功")
    except Exception as e:
        print("关闭出现异常：", str(e))


def accept_client(server):
    """
    服务端不断的接收客户端的连接
    :param server: Socket服务端对象
    :return
    """

    while True:
        client_conn, client_address = server.accept()
        ip = client_address[0]
        port = client_address[1]

        time_now = time.strftime('%Y-%m-%d %H:%M:%S')
        print("{} \t新的客户端：ip:{},port:{}".format(time_now, ip, port))
        print(id(client_conn))

        # 判断ip的key是否已经在client_dict中
        # 如果在，就需要关闭client，然后把新的conn加入到dict中
        if ip in client_dict:
            # 关闭老的连接
            conn_old = client_dict[ip]
            close_client_connect(conn_old)

        # 把新的连接加入到client_dict中
        client_dict[ip] = client_conn

        # 启动接收客户端消息的线程
        t = threading.Thread(target=recv_client_message, args=(client_conn, client_address))
        t.start()


def main():
    # 创建一个socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 建立连接
    server_address = ('0.0.0.0', 9000)
    server.bind(server_address)

    # 开始捕获连接
    server.listen(10)

    # 启动不断监控新的连接的线程
    t = threading.Thread(target=accept_client, args=(server,))
    # 启动线程
    t.start()

    # 等待线程结束：其实accept_client是个死循环，会会一直在执行
    t.join()


if __name__ == "__main__":
    # 程序开始执行
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    print("{}:start".format(now))
    main()
    print("Done")
