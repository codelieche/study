# -*- coding:utf-8 -*-
"""
对数组进行排序
"""
import random


def find_smallest_item_index(array):
    """
    找到数组中最小元素的索引
    :param array: 数组
    :return:
    """
    # 1. 先初始化最小的元素和，最小元素的索引
    smallest = array[0]
    smallest_index = 0

    # 2. 从元素第2个元素开始一个一个比对，小于smallest，那么最小的值就变更
    for index in range(1, len(array)):
        if array[index] < smallest:
            # 小于最小值，那么当前这个值才是最小的
            smallest = array[index]
            smallest_index = index

    # 3. 返回最小元素的索引
    return smallest_index


def array_sort(array):
    """
    对数组进行排序
    :param array: 数组
    :return: 排序后的数组【从小到大的哦】
    """
    # 1. 用new_array保存排序后的数组
    new_array = []

    # 2. array有多少个元素，就需要执行多少次 找出最小元素的操作
    for i in range(len(array)):
        # 2-1：找出array中的最小元素索引
        smallest_index = find_smallest_item_index(array)

        # 2-2: 把这个最小的元素从array中移除，然后加入到new_array中
        new_array.append(array.pop(smallest_index))

    # 3. 返回新的数组
    return new_array


def main():
    """
    执行数组排序的操作
    """
    # 1. 随机生成个10-30个元素的数组
    array = [random.randint(1, 1000) for _ in range(random.randint(10, 30))]
    print("未排序前数组是：\n\t{}".format(array))

    # 2. 对数组进行排序
    new_array = array_sort(array=array)
    print("排序后数组是：\n\t{}".format(new_array))


if __name__ == "__main__":
    # 对数组进行排序
    for i in range(1, 6):
        print("========第{}次执行=========".format(i))
        main()
        print("\n")
