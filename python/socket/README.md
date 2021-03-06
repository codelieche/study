## Socket

> Socket是网络编程的一个抽象概念。通常我们一个Socket表示“打开了一个网络链接”，  
而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。

### 客户端

> 大多数连接都是可靠的TCP连接。创建TCP连接的时候，主动发起连接的一方叫**客户端**，
被动响应连接的叫**服务器**。

### Socket类型
套接字格式：socket(family, type[,protocal]) 使用给定的套接族，套接字类型，协议编号（默认为0）来创建套接字

socket 类型 | 描述 
:--- | :---
socket.AF_UNIX | 用于同一台机器上的进程通信（既本机通信）
socket.AF_INET | 用于服务器与服务器之间的网络通信
socket.AF_INET6 | 基于IPV6方式的服务器与服务器之间的网络通信
socket.SOCK_STREAM | 基于TCP的流式socket通信
socket.SOCK_DGRAM | 基于UDP的数据报式socket通信
socket.SOCK_RAW | 原始套接字，普通的套接字无法处理ICMP、IGMP等网络报文，而SOCK_RAW可以；其次SOCK_RAW也可以处理特殊的IPV4报文；此外，利用原始套接字，可以通过IP_HDRINCL套接字选项由用户构造IP头
socket.SOCK_SEQPACKET | 可靠的连续数据包服务

### TCP 与 UDP
- TCP是面向连接的，UDP是面向非连接的
- TCP发送数据时，已建立好TCP链接，所以不需要指定地址，而UDP是面向无连接的，每次发送都需要指定发送给谁
- 服务器与客户端不能直接发送列表，元素，字典等带有数据类型的格式，发送的内容必须是字符串数据

**创建TCP Socket**：
```
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

**创建UDP Socket**：
```
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

### Socket函数

**服务器端 Socket 函数**

Socket 函数 | 描述
:--- | :---
s.bind(address) | 将套接字绑定到地址，在AF_INET下，以tuple(host, port)的方式传入，如s.bind((host, port))
s.listen(backlog) | 开始监听TCP传入连接，backlog指定在拒绝链接前，操作系统可以挂起的最大连接数，该值最少为1，大部分应用程序设为5就够用了
s.accept() | 接受TCP链接并返回（conn, address），其中conn是新的套接字对象，可以用来接收和发送数据，address是链接客户端的地址。

**客户端 Socket 函数**

Socket 函数 | 描述
:--- | :---
s.connect(address) | 链接到address处的套接字，一般address的格式为tuple(host, port)，如果链接出错，则返回socket.error错误
s.connect_ex(address) | 功能与s.connect(address)相同，但成功返回0，失败返回errno的值

**公共 Socket 函数**

Socket 函数 | 描述
:--- | :---
s.recv(bufsize[, flag]) | 接受TCP套接字的数据，数据以字符串形式返回，buffsize指定要接受的最大数据量，flag提供有关消息的其他信息，通常可以忽略
s.send(string[, flag]) | 发送TCP数据，将字符串中的数据发送到链接的套接字，返回值是要发送的字节数量，该数量可能小于string的字节大小
s.sendall(string[, flag]) | 完整发送TCP数据，将字符串中的数据发送到链接的套接字，但在返回之前尝试发送所有数据。成功返回None，失败则抛出异常
s.recvfrom(bufsize[, flag]) | 接受UDP套接字的数据u，与recv()类似，但返回值是tuple(data, address)。其中data是包含接受数据的字符串，address是发送数据的套接字地址
s.sendto(string[, flag], address) | 发送UDP数据，将数据发送到套接字，address形式为tuple(ipaddr, port)，指定远程地址发送，返回值是发送的字节数
s.close() | 关闭套接字
s.getpeername() | 返回套接字的远程地址，返回值通常是一个tuple(ipaddr, port)
s.getsockname() | 返回套接字自己的地址，返回值通常是一个tuple(ipaddr, port)
s.setsockopt(level, optname, value) | 设置给定套接字选项的值
s.getsockopt(level, optname[, buflen]) | 返回套接字选项的值
s.settimeout(timeout) | 设置套接字操作的超时时间，timeout是一个浮点数，单位是秒，值为None则表示永远不会超时。一般超时期应在刚创建套接字时设置，因为他们可能用于连接的操作，如s.connect()
s.gettimeout() | 返回当前超时值，单位是秒，如果没有设置超时则返回None
s.fileno() | 返回套接字的文件描述
s.setblocking(flag) | 如果flag为0，则将套接字设置为非阻塞模式，否则将套接字设置为阻塞模式（默认值）。非阻塞模式下，如果调用recv()没有发现任何数据，或send()调用无法立即发送数据，那么将引起socket.error异常。
s.makefile() | 创建一个与该套接字相关的文件

----

### Socket编程思想

#### TCP服务器

**1. 创建套接字，丙丁套接字到本地IP与端口**

```python
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('0.0.0.0', 9000)
s.bind(server_address)
```

**2. 开始监听连接**

```python
server.listen(5)
```

**3. 进入循环，不断的将接受客户端的链接请求**

```python
while True:
    conn, address = server.accept()
```

**4. 接收客户端传来的数据，并且发送数据给对方**

```python
conn.recv(1024)
conn.sendall()
```

**5. 传输完毕后，关闭套接字**

```python
server.close()
```

#### TCP客户端

**1. 创建套接字并连接至远端地址**

```python
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 9000)
client.connect(server_address)
```

**2. 连接后发送数据和接收数据**

```python
client.sendall(b'Hello World')

client.recv(1024)
```

**3. 传输完毕，关闭套接字**

```python
client.close()
```


