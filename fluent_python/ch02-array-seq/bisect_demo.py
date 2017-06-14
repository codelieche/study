# -*- coding:utf-8 -*-
import bisect
import sys
import random

# 干草垛，一个有序的序列
HAYSTACK = [random.randint((i-1) * 3, i * 3) for i in range(1, 15)]
# 针，需要插入的值
NEEDLES = [random.randint((i-1) * 3, i * 3) for i in range(1, 12)]

# row format
ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'


def demo(bisect_fun):
    for needle in reversed(NEEDLES):
        position = bisect_fun(HAYSTACK, needle)
        # 下面是打印，方便查看插入的位置信息
        # 空格不匹配，答应出来的值就不对
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))


if __name__ == "__main__":
    # 通过参数来确定是用bisect_left还是bisect_right函数
    if sys.argv[-1] == 'left':
        bisect_fun = bisect.bisect_left
    else:
        bisect_fun = bisect.bisect_right

    print('Demo:', bisect_fun.__name__)
    print("HAYSTACK: {}".format(HAYSTACK))
    print("NEEDLES: {}".format(NEEDLES))
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fun)

