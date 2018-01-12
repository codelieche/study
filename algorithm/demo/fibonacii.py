# -*- coding:utf-8 -*-
"""
斐波那契
"""
import random


def fibonacii(n):
    """
    用递归方法计算fibnacci
    :param n:
    :return:
    """
    if n < 0:
        return 0

    if n <= 2:
        return 1
    else:
        return fibonacii(n-1) + fibonacii(n-2)


def fibonacii_while(n):
    """
    用循环的方式计算斐波那契的值
    :param n:
    :return:
    """
    i, a, b = 0, 0, 1
    while i < n:
        a, b = b, a + b
        i = i + 1
    return a


def main_fib_01():
    for i in range(10):
        n = random.randint(1, 30)
        fib = fibonacii(n)
        print(n, '===>', fib)


def main_fib_02():
    for i in range(10):
        n = random.randint(1, 30)
        fib = fibonacii_while(n)
        print(n, '===>', fib)


def main_fib():
    for i in range(10):
        n = random.randint(1, 30)
        fib_01 = fibonacii(n)
        fib_02 = fibonacii_while(n)
        print(n, '===>', fib_01, fib_02)


if __name__ == "__main__":
    # main_fib_01()
    # main_fib_02()
    main_fib()
