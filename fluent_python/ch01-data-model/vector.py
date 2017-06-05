# -*- coding:utf-8 -*-
"""
一个简单的二维向量
"""

from math import hypot
# hypot 是求三角形的斜边长


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        # obj显示的会是 Vector(x, y)，而不是<__main__.Vector instance at 0x107b9b3f8>
        return 'Vector({}, {})'.format(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == "__main__":
    v1 = Vector(5, 6)
    v2 = Vector(3, 4)
    print(v1)  # Vector(5, 6)
    print(v1 + v2)  # Vector(8, 10)
    print(v1 * 4)  # Vector(20, 24)
    print(abs(v2))  # 5.0

