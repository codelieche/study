# -*- coding:utf-8 -*-
from random import random
# 先引入array
from array import array

# 利用一个可迭代对象，建立一个双精度浮点数array（类型是`d`）
# floats用的可迭代对象是一个生成器：(random() for i in range(10**7))
floats = array('d', (random() for i in range(10**7)))

# 调试一个出来卡看看
floats[-10]  # 0.20539555866224857
fp = open('floats.bin', 'wb')
# 把数组存入一个二进制文件中
floats.tofile(fp)
fp.close()

# 创建一个新的双精度浮点空数组
floats2 = array('d')
fp2 = open('floats.bin', 'rb')
# 从fp2中读取数据
floats2.fromfile(fp2, 10**7)
fp2.close()

# 调试个内容看看，与floats[-10]是相同的
floats2[-10]  # 0.20539555866224857

# 注意：他们的id虽然不同，但是内容是相同的，完全一样
print(id(floats2))  # 4397490840
print(id(floats))  # 4397407736
print(floats == floats2)  # True
print(floats is floats2)  # False
