# -*- coding:utf-8 -*-
"""
这个是分布式根据消息处理数据的程序
"""

import time
import sys
import os
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


# 由于这个QueueManager只从网络上获取Queue, 所以注册时只提供名字
QueueManager.register('get_queue_task')
QueueManager.register('get_queue_result')


# 连接到服务器，也就是运行task.master.py的机器
master_addr = '127.0.0.1'
print('Connect to Server %s' % master_addr)

# 端口和验证码注意保持一致，佛者连接失败
m = QueueManager(address=(master_addr, 5000), authkey='123456')

# 从网络连接
m.connect()
task = m.get_queue_task()
result = m.get_queue_result()
# 从task队列取任务，并把结果写入result队列

print('Worker %s start!' % os.getpid())

for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Exception as e:
        print(e)
        print('task queue is empty')

print('Worker %s Done!' % os.getpid())
