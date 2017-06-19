#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
继承UserDict,
"""
try:
    from collections import UserDict
except ImportError as e:
    print(e)
    from UserDict import UserDict


class StrKeyDict(UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, value):
        self.data[str(key)] = value

if __name__ == "__main__":
    d = StrKeyDict([(2, 'two'), ('4', 'four')])
    print(d[2])  # two
    print(d[4])  # four
