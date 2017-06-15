# -*- coding:utf-8 -*-
import bisect
import random

SIZE = 7

# 置随机数种子
random.seed(1234)

my_list = []
for i in range(SIZE):
    # 随机生成一个值，每次区间是[0, size *2]
    new_item = random.randrange(SIZE * 2)
    # 把新的值插入到my_list中，并且my_list保存有序
    bisect.insort(my_list, new_item)
    print('%2d -> %s' % (new_item, my_list))
