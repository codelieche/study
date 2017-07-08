# 第4章：文本和字节序列
> 人类使用文本，计算机使用字节序列。

## 4.1 字符问题
> 把码位转换成字节序列的过程是**编码**(`encode`)；把字节序列转换成码位的过程是**解码**(`decode`).  
或者说：把人看的懂的(文本)转成机器看得懂的(字节序列)叫做**编码**;把机器看的懂的(字节序列)转成人看的懂的(文本)叫**解码**。

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
> Python内置了两种基本的二进制序列类型：Python3引入的不可变bytes类型和Python2.6添加的可变bytearray类型。  
（Python2.6也引入了bytes类型，单那只不过是str类型的别名，与Python3的bytes类型不同。）

bytes或bytearray对象的各个元素是介于0~255(含)之间的整数，而不像Python2的str对象那样是个单个的字符。

```
In [19]: china = bytes('中国', encoding='utf-8')

In [20]: china
Out[20]: b'\xe4\xb8\xad\xe5\x9b\xbd'

In [21]: china[0]
Out[21]: 228

In [22]: china[:1]
Out[22]: b'\xe4'

In [23]: china_arr = bytearray(china)

In [24]: china_arr
Out[24]: bytearray(b'\xe4\xb8\xad\xe5\x9b\xbd')

In [25]: china_arr[-1:]
Out[25]: bytearray(b'\xbd')
```
> 二进制序列的切片始终是同一类型的二进制序列，包括长度为1的切片。

## 4.3 基本的编解码器

## 4.4 了解编解码问题
- `UnicodeEncodeError`: 把字符串转成二进制序列时出错
- `UnicodeDecodeError`: 把二进制序列转换成字符串时出错

## 4.5 处理文本文件

## 4.6 为了正确比较而规范化Unicode字符串

## 4.7 Unicode文本排序

## 4.8 Unicode数据库

## 4.9 支持字符串和字节序列的双模式API


> MacOS系统下执行：

```
In [31]: import sys

In [32]: sys.getdefaultencoding()
Out[32]: 'utf-8'

In [33]: sys.getfilesystemencoding()
Out[33]: 'utf-8'

In [34]: import locale

In [35]: locale.getpreferredencoding()
Out[35]: 'UTF-8'

In [36]: sys.stdout.encoding
Out[36]: 'UTF-8'
```

> Debian系统下执行：

```
>>> import sys
>>> print(sys.getdefaultencoding())
ascii
>>> print(sys.getfilesystemencoding())
UTF-8
>>> print(sys.stdout.encoding)
UTF-8
>>> import locale
>>> print(locale.getpreferredencoding())
UTF-8
```
