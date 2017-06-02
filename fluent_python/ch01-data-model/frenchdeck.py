# -*- coding:utf-8 -*-

from collections import namedtuple


def demo_01():
    # nametuple simple demo
    User = namedtuple("User", ('name', 'age'))
    u1 = User("Jim", 20)
    u2 = User(name="Tom", age=26)
    print(u1.age, u1.name)
    print(u2.name, u2.age)
    print(u2[0], u2[1])


if __name__ == "__main__":
    demo_01()
