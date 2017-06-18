# -*- coding:utf-8 -*-
"""
统计单词
"""
import re
from collections import Counter

desc = """
Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.
The Python interpreter and the extensive standard library are freely available in source or binary form for all major platforms from the Python Web site, https://www.python.org/, and may be freely distributed. The same site also contains distributions of and pointers to many free third party Python modules, programs and tools, and additional documentation.
The Python interpreter is easily extended with new functions and data types implemented in C or C++ (or other languages callable from C). Python is also suitable as an extension language for customizable applications.
This tutorial introduces the reader informally to the basic concepts and features of the Python language and system. It helps to have a Python interpreter handy for hands-on experience, but all examples are self-contained, so the tutorial can be read off-line as well.
For a description of standard objects and modules, see The Python Standard Library. The Python Language Reference gives a more formal definition of the language. To write extensions in C or C++, read Extending and Embedding the Python Interpreter and Python/C API Reference Manual. There are also several books covering Python in depth.
This tutorial does not attempt to be comprehensive and cover every single feature, or even every commonly used feature. Instead, it introduces many of Python’s most noteworthy features, and will give you a good idea of the language’s flavor and style. After reading it, you will be able to read and write Python modules and programs, and you will be ready to learn more about the various Python library modules described in The Python Standard Library.
"""


def word_counter_01():
    re_word = re.compile(r'\w+')
    re_word_result = re_word.findall(desc)
    print(re_word_result[:6])
    word_counter_dic = {}
    for word in re_word_result:
        # 统计单词出现的次数
        if word in word_counter_dic:
            word_counter_dic[word] += 1
        else:
            word_counter_dic[word] = 1
    # 全部统计完毕
    for k, v in word_counter_dic.items():
        print("{:15}出现次数:{:>3}".format(k, v))


def word_counter_02():
    re_word = re.compile(r'\w+')
    re_word_result = re_word.findall(desc)
    # 使用内置的Counter类直接统计
    c = Counter(re_word_result)
    print(type(c))
    # 答应出最多的5个单词
    for word, num in c.most_common(5):
        print("{:15}出现次数:{:3}".format(word, num))


if __name__ == "__main__":
    # 方式一
    word_counter_01()
    # 方式二
    word_counter_02()
