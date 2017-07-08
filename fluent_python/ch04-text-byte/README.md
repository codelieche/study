# 第4章 文本和字节序列
> 人类使用文本，计算机使用字节序列。

## 4.1 字符问题
> 把码位转换成字节序列的过程是**编码**(`encode`)；把字节序列转换成码位的过程是**解码**(`decode`).  
或者说：把人看的懂的(文本)转成机器看得懂的(字节)叫做**编码**;把机器看的懂的(字节)转成人看的懂的(文本)叫**解码**。

```
In [10]: s
Out[10]: '中国'

In [11]: len(s)
Out[11]: 2

In [12]: s2 = s.encode('utf8')

In [13]: s2
Out[13]: b'\xe4\xb8\xad\xe5\x9b\xbd'

In [14]: len(s2)
Out[14]: 6

In [15]: s2.decode('utf-8')
Out[15]: '中国'

In [18]: print(type(s),type(s2))
<class 'str'> <class 'bytes'>
```
**注意：**以上代码使用python3演示。

> 虽然Python3的str类型相当于Python2的unicode类型，只不过是换了个新的名称。  
但是Python3的bytes类型却不是把str类型转换个名称那么简单，而且还有关系紧密的bytearray类型。

## 4.2 字节概要

