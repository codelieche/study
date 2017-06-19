# -*- coding:utf-8 -*-
"""
映射类型里的键统统转换成str
"""


class StrKeyDict0(dict):
    def __missing__(self, key):
        # 当有非字符串的键被查找的时候，StrKeyDict0把键转换为字符串
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

if __name__ == "__main__":
    d = StrKeyDict0([('2', 'two'), ('3', 'three')])
    print(d['2'])  # two
    print(d[2])  # two
    # print(d[4])   # KeyError: '4'
    print(d.get(4, 'no'))  # no
    print(d.get(2))  # two
