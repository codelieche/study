# -*- coding:utf-8 -*-
"""
二分查找
"""
import random


def binary_search(source_list, item):
    """
    二分查找
    :param source_list: 要查找的列表
    :param item: 要查找的元素
    :return: item的索引或者None
    """
    # 最小下标和最大下标
    low = 0
    high = len(source_list) - 1

    # 开始查找
    while low <= high:
        # 检查中间的元素
        mid = (low + high) // 2
        # 要检查的元素值
        guess = source_list[mid]
        if guess == item:
            return mid
        elif guess > item:
            # 猜的数字大了
            # 新的上界为： 中间值 - 1
            high = mid - 1
        else:
            # 猜的值小了
            # 新的下界从：中间值 + 1 开始
            low = mid + 1
    return None


if __name__ == "__main__":
    source = list(range(1, 100, 2))
    target_item = random.randint(1, 100)
    print("要查找的列表：", source)
    print("要查找的元素是：", target_item)
    result = binary_search(source, target_item)
    if result:
        print("\t元素{}在列表中，索引为:{}".format(target_item, result))
    else:
        print("\t元素{}【不在列表中】".format(target_item))
