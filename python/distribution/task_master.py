# -*- coding:utf-8 -*-
"""
分布式主进程
"""

import time
import queue
import random
from multiprocessing.managers import BaseManager

# 发送任务点的队列
queue_task = queue.Queue()
# 接收结果的队列
queue_result = queue.Queue()


# 自定义QueueManager
class QueueManager(BaseManager):
    pass

# 把两个Queue注册到网络上
QueueManager.register('get_queue_task', callable=lambda: queue_task)
QueueManager.register('get_queue_result', callable=lambda: queue_result)

# 绑定端口8081，设置验证码：'123456'
manager = QueueManager(address=('', 5000), authkey='123456')

# 启动Queue
manager.start()

# 获取通过网络访问的Queue对象
task = manager.get_queue_task()
result = manager.get_queue_result()

print('%s: Start!' % time.strftime('%Y-%m-%d %H-%M-%S'))
# 放些任务进去
for i in range(10):
    n = random.randint(100, 1000)
    print('Put task %d...' % n)
    task.put(n)

# 从result队列中读取结果
print("开始读取结果")
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)

# 关闭
manager.shutdown()
print('%s: Done!' % time.strftime('%Y-%m-%d %H-%M-%S'))

