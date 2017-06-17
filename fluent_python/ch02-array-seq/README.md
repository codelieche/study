# 第2章：序列构成的数组

> Python不管是哪种数据结构，字符串、列表、字节序列、数组、XML元素，抑或是数据库查询结果，  
他们都共用一套丰富的操作：迭代、切片、排序，还有拼接。

## 2.1：内置序列类型概览
- 容器序列：`list`,`tuple`,`collection.deque`这些序列能存放不同类型的数据
- 扁平序列：`str`,`bytes`,`bytearray`,`memoryview`和`array.array`这类序列只能容纳一种类型

> **容器序列**存放的是它们所包含的任意类型的对象的引用，而**扁平序列**里存放的是值而不是引用。  
换句话说：扁平序列其实是一段连续的内存空间。  
由此可见扁平序列其实更加紧凑，但是它里面只能存放诸如字符、字节和数值这种基础类型。

- 按照能否被修改来分类：
    1. 可变序列：`list`,`bytearray`,`array.array`,`collections.deque`和`memoryview`
    2. 不可变序列：`tuple`,`str`和`bytes`。

## 2.2：列表推导和生成器表达式

> 列表推导是构建列表（list）的快捷方式，而生成器表达式则可以用来创建其他任何类型的序列。  
list comprehension简称listcomps, generator expression简称genexps。

### 2.2.1 列表推导和可读性

#### 注意事项
- 只用列表推导来创建新的列表，并且尽量保持简短（太长了还是用for来写）
- 列表推导，for关键词之后的赋值操作可能会影响列表推导上下文中的同名变量（py3中不会）

方式一：

```
>>> symbols = "$%^&*("
>>> codes = []
>>> for symbol in symbols:
...     codes.append(ord(symbol))
... 
>>> codes
[36, 37, 94, 38, 42, 40]
```

方式二：

```
>>> symbols = "$%^&*("
>>> codes = [ord(symbol) for symbol in symbols]
>>> codes
[36, 37, 94, 38, 42, 40]
```

> 把`[]`改成`()`就是**生成器**对象了。

```
>>> codes2 = (ord(symbol) for symbol in symbols)
>>> codes2
<generator object <genexpr> at 0x108e2caa0>
>>> for code in codes2: print(code)
...
36 37 94 38 42 40
```

### 2.2.2 列表推导同filter和map的比较
> filter和map合起来能做的事情，列表推导也可以做，而且还不需要用lambda。

```
>>> symbols = "*&()_+!@dΛΞΟΠΡΣ"
>>> beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
>>> beyond_ascii
[206, 155, 206, 158, 206, 159, 206, 160, 206, 161, 206, 163]
>>> beyond_ascii = list(filter(lambda c:c > 127, map(ord, symbols)))
>>> beyond_ascii
[206, 155, 206, 158, 206, 159, 206, 160, 206, 161, 206, 163]
```

### 2.2.3 笛卡尔积

> 笛卡尔积是一个列表，列表里的元素是由输入的可迭代类型的元素对构成的元组。  
比如：12种牌(2-10 jKQA)，4种花色，笛卡尔积长度就是13*4=52。

#### 使用列表推导计算笛卡尔积

```
>>> sizes = ['S', 'M', 'L']
>>> tshirts = [(color, size) for color in colors for size in sizes]
>>> for tshirt in tshirts: print tshirt
...
('black', 'S')
('black', 'M')
('black', 'L')
('white', 'S')
('white', 'M')
('white', 'L')
```

### 2.2.4 生成器表达式
> 生成器表达式背后遵循了迭代器协议，可以逐个地产出元素。  
而不是先建立一个完整的列表，然后再把这个列表传递到某个构造函数里。


## 2.3：元组
> 元组不仅仅是不可变的列表。

### 2.3.2 元组拆包

```
>>> lax_coordinates = (33.9425, -118.408056)
>>> latitude, longitude = lax_coordinates
>>> latitude
33.9425
>>> longitude
-118.408056
>>> _, x = ('xyz', 123)
>>> x
123
```

**用*来处理剩下的元素**  
在Python中，函数用`*args`来获取不确定数量的参数，`**kwargs`获取不确定的键值对参数。

```
>>> x, y, *z = range(5)
>>> z
[2, 3, 4]
>>> a, *b, c,d = range(5)
>>> b
[1, 2]
```
**注意**：在python2中会报错.

### 2.3.3 嵌套元组拆包

### 2.3.4 具名元组
> 命名元组：`collections.namedtuple`,2个参数，一个是类名，另一个是类的各个字段的名字。  
后者可以是由数个字符串组成的可迭代对象，或者是由空格分割的字段名组成的字符串。

```python

from collections import namedtuple
User = namedtuple("User", ('name', 'age'))

City = namedtuple("City", 'name country population coordinates')
print(City._fields)  # ('name', 'country', 'population', 'coordinates')
u = User._make(('Jim', 20))  # User(name='Jim', age=20)
u._asdict()  # OrderedDict([('name', 'Jim'), ('age', 20)])
```

- `_fields`：类属性，一个包含这个类所有字段名称的元组
- `_make(iterable)`：类方法，通过接受一个可迭代对象来生成这个类的一个实例，它的作用跟`ClassName(*iter)`是一样的
- `_asdict()`: 实例方法，把具名元组以`collections.OrderedDict`的形式返回

### 作为不可变列表的元组


## 2.4：切片

### 2.4.1 为什么切片和区间会忽略最后一个元素
- 当只有最后一个**位置**信息时，我们也可以快速看出切片和区间里有几个元素：`range(3)`和`my_list[:3]`都返回3个元素
- 当起止位置信息都可见时，我们可以快速计算出切片和区间的长度，用`(stop - start)`即可
- 利用任意一个下标来把序列分割成不重叠的两部分，`my_list[:x]`和`my_list[x:]`以下标`x`分割

### 2.4.2 对对象进行切片
- `my_list[a:b:c]`：对my_list在a和b之间以c为间隔取值，c的值可以为负数（反着取）

```
>>> s = 'python is good'
>>> s[::3]
'ph  o'
>>> s[::-1]
'doog si nohtyp'
>>> slice(0,6)
slice(0, 6, None)
>>> s[slice(0,6)]
'python'
```

### 给切片赋值

```
>>> a = list(range(10))
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a[2:5]
[2, 3, 4]
>>> a[2:5] = [20, 'aaa', 50]
>>> a
[0, 1, 20, 'aaa', 50, 5, 6, 7, 8, 9]
```

## 2.5: 对序列使用+和*

## 2.6：序列的增量赋值

> `+=`背后的特殊方法是：`__iadd__`(用于“就地加法”)，如果一个类没有实现这个方法的话，Python会退一步调用`__add__`。  
如果不是就地加法，`a = a + b`首先计算`a + b`，得到一个新的对象，然后赋值给`a`。  
总体来说：可变序列一般都实现了`__iadd__`方法，因此`+=`是就地加法。  
`*=`对应的是`__imul__`。

**一个关于+=的谜题：**

```
>>> t = (1, 2, [3, 4], 5)
>>> t[2] += ['a', 'b', 'c']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> t
(1, 2, [3, 4, 'a', 'b', 'c'], 5)
```

**说明：** t是不可变的当对其元素重新赋值，它会抛出`TypeError`异常，同时`t[2]`是列表，它可变，赋值成功。  
**注意：**不要把可变的对象放入元组中。

## 2.7 list.sort方法和内置函数sorted
> list.sort方法会就地排序列表，不会把原列表复制一份。其返回值是None哦！  
`sorted`函数，它会新建一个列表作为返回值。

```
>>> import random
>>> l = [random.randint(10, 100) for _ in range(10)]
>>> l
[61, 91, 19, 29, 78, 40, 66, 33, 59, 20]
>>> print(l.sort())
None
>>> l
[19, 20, 29, 33, 40, 59, 61, 66, 78, 91]
>>> random.shuffle(l)  # 对l重新搅乱
>>> l
[61, 19, 59, 66, 40, 29, 91, 78, 20, 33]
>>> print(sorted(l))  # 用sorted排序
[19, 20, 29, 33, 40, 59, 61, 66, 78, 91]
>>> l   # sorted排序后，l没变化
[61, 19, 59, 66, 40, 29, 91, 78, 20, 33]
```

> 一个函数或者方法，对对象进行的是就地改动，那它就应该返回`None`。  
eg:`random.shuffle`。shuffle：洗牌、搅乱。

### list.sort和sorted的参数
- `reverse`: 默认是`False`，从低到高排序，设置为`True`将从高到低排序
- `key`: 一个只有一个参数的函数，这个函数会被用在序列的每个元素上，所产生的结果将是排序算法依赖的对比关键字。

```
>>> import string    
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> l2 = [''.join(random.sample(string.ascii_letters, random.randint(1, 5))) for _ in range(0, 5)]
>>> l2
['AdS', 'B', 'bwd', 'HadBM', 'Xa']
>>> sorted(l2)
['AdS', 'B', 'HadBM', 'Xa', 'bwd']
>>> sorted(l2, key=lambda x: len(x))
['B', 'Xa', 'AdS', 'bwd', 'HadBM']
>>> sorted(l2, key=lambda x: len(x), reverse=True)
['HadBM', 'AdS', 'bwd', 'Xa', 'B']
```

## 2.8 用bisect来管理已排序的序列
> bisect(平分、二等分)模块包含两个主要函数，bisect和insort，两个函数都利用二分查找算法来在有序序列中查找或插入元素。

```
>>> import bisect
>>> dir(bisect)
['bisect', 'bisect_left', 'bisect_right', 'insort', 'insort_left', 'insort_right']
```

### bisect.bisect

> bisect(a, x[, lo[, hi]]) -> index  
Return the index where to insert item x in list a, assuming a is sorted.

> `bisect(haystack, needle)`在haystack(干草垛)里搜索needle(针)的位置，  
该位置满足的条件是，把needle插入这个位置后，haystack还能保持升序。返回的是出入的位置索引(index)。  
也就是index左边的值都小于或者等于needle。  
注意：haystack必须是一个有序的序列。  

得到索引怎么用呢？  
用bisect.bisect得到了所以，再用haystack.insert(index, needle)来插入新值。

```
>>> l = [1, 2, 4, 6, 8]
>>> bisect.bisect(3)
>>> bisect.bisect(l, 3)
2
>>> l
[1, 2, 4, 6, 8]
>>> l.insert(bisect.bisect(l,3), 3)
>>> l
[1, 2, 3, 4, 6, 8]
```

### 示例：python3 bisect_demo.py

```
Demo: bisect_right
HAYSTACK: [3, 4, 6, 12, 14, 18, 19, 22, 24, 28, 33, 34, 36, 41]
NEEDLES: [0, 6, 7, 9, 12, 18, 20, 22, 24, 29, 33]
haystack ->  3  4  6 12 14 18 19 22 24 28 33 34 36 41
33 @ 11      |  |  |  |  |  |  |  |  |  |  |33
29 @ 10      |  |  |  |  |  |  |  |  |  |29
24 @  9      |  |  |  |  |  |  |  |  |24
22 @  8      |  |  |  |  |  |  |  |22
20 @  7      |  |  |  |  |  |  |20
18 @  6      |  |  |  |  |  |18
12 @  4      |  |  |  |12
 9 @  3      |  |  |9 
 7 @  3      |  |  |7 
 6 @  3      |  |  |6 
 0 @  0    0 
 
Demo: bisect_left
HAYSTACK: [2, 5, 6, 10, 15, 15, 19, 21, 27, 28, 33, 36, 36, 40]
NEEDLES: [2, 6, 6, 10, 15, 15, 19, 23, 27, 27, 32]
haystack ->  2  5  6 10 15 15 19 21 27 28 33 36 36 40
32 @ 10      |  |  |  |  |  |  |  |  |  |32
27 @  8      |  |  |  |  |  |  |  |27
27 @  8      |  |  |  |  |  |  |  |27
23 @  8      |  |  |  |  |  |  |  |23
19 @  6      |  |  |  |  |  |19
15 @  4      |  |  |  |15
15 @  4      |  |  |  |15
10 @  3      |  |  |10
 6 @  2      |  |6 
 6 @  2      |  |6 
 2 @  0    2 
```

> 如果要插入的值，在序列中存在，那么这个插入的值是放已经存在的值，左边还是右边？  
`bisect_left`和`bisect_right`的差异就在这里。

### 用bisect.insort插入新元素

```
>>> l
[1, 2, 3, 4, 6, 8]
>>> bisect.insort(l, 5)
>>> l
[1, 2, 3, 4, 5, 6, 8]
>>> bisect.insort_left(l, 6)
>>> l
[1, 2, 3, 4, 5, 6, 6, 8]
```

insort可以保持有序序列的顺序：另外也有`(insort_left, insort_right)`

```
➜  ch02-array-seq git:(master) ✗ python bisect_insort.py 
13 -> [13]
 6 -> [6, 13]
 0 -> [0, 6, 13]
12 -> [0, 6, 12, 13]
13 -> [0, 6, 12, 13, 13]
 8 -> [0, 6, 8, 12, 13, 13]
 9 -> [0, 6, 8, 9, 12, 13, 13]
```

## 2.9 当列表不是首选项时

### 数组 Arrays
> 如果我们需要一个只包含数字的列表，那么`array.array`比`list`更高效。  
array.array支持所有跟可变序列有关的操作，比如：`pop`、`insert`和`extend`。  
另外，array还提供从文件读取和存入文件的更快的方法，`.frombytes`和`.tofile`。

#### array Type Code

Type code |  C Type | Minimum size in bytes
-------- | --------- | ------- | -------
 'c' |    character  　　| 1
 'b' |    signed integer 　　| 1
 'B' |    unsigned integer   　　| 1
 'u' |    Unicode character  　　| 2
 'h' |    signed integer 　　| 2
 'H' |    unsigned integer  | 2
 'i' |    signed integer  | 2
 'I' |    unsigned integer  | 2
 'l' |    signed integer  | 4
 'L' |    unsigned integer  | 4
 'f' |    floating point | 4
 'd' |    floating point  | 8

**示例：创建1000万个随机浮点数的数组：**

```python

from random import random
# 先引入array
from array import array

# 利用一个可迭代对象，建立一个双精度浮点数array（类型是`d`）
# floats用的可迭代对象是一个生成器：(random() for i in range(10**7))
floats = array('d', (random() for i in range(10**7)))

# 调试一个出来卡看看
floats[-10]  # 0.20539555866224857
fp = open('floats.bin', 'wb')
# 把数组存入一个二进制文件中
floats.tofile(fp)
fp.close()

# 创建一个新的双精度浮点空数组
floats2 = array('d')
fp2 = open('floats.bin', 'rb')
# 从fp2中读取数据
floats2.fromfile(fp2, 10**7)
fp2.close()

# 调试个内容看看，与floats[-10]是相同的
floats2[-10]  # 0.20539555866224857

# 注意：他们的id虽然不同，但是内容是相同的，完全一样
print(id(floats2))  # 4397490840
print(id(floats))  # 4397407736
print(floats == floats2)  # True
print(floats is floats2)  # False
```

> 另外我们也可以使用`pickle`模块，来把一些Python数据保存到文件中。

```
>>> import pickle
>>> d = {'name': 'Tom', 'age': 20}
>>> d
{'age': 20, 'name': 'Tom'}
>>> pickle.dump(d, open('test.bin', 'wb'))
>>> d2 = pickle.load(open('test.bin', 'rb'))
>>> d2
{'age': 20, 'name': 'Tom'}
>>> d2 == d
True
>>> d is d2
False
```

### 2.9.2 内存视图（Memory views）
> memoryview是一个内置类，它能让用户在不复制内容的情况下操作同一个数组的不同切片。  
memoryview.cast的概念跟数组模块类似，能用不同的方式读写同一块内存数据，而且内容字节不会随意改动。  
memoryview.cast会把同一块内存里的数据内容打包成一个全新的memoryview对象给你。

```
>>> import array
>>> numbers = array.array('h', [-4, -2, 0, 2, 4])
>>> memv = memoryview(numbers)
>>> len(memv)
5
>>> memv_oct = memv.cast('B')
>>> mvmv_oct.tolist()
[252, 255, 254, 255, 0, 0, 2, 0, 4, 0]
>>> memv_oct[5] = 4
>>> numbers
array('h', [-4, -2, 1024, 2, 4])
```
把memv里面的内容转换成`B`类型，赋值给`memv_oct`(无符号字符)。  
当把memv_oct位置为5的字节赋值成4。  
注意：是在python3中测试的。

### 2.9.3 NumPy and SciPy

```
>>> import numpy as np
>>> a = np.arange(12)
>>> a
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
>>> type(a)
<type 'numpy.ndarray'>
>>> a.shape
(12,)
>>> a.shape = (3, 4)
>>> a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> a[2]
array([ 8,  9, 10, 11])
>>> a[2, 2]
10
>>> a[:, 1]
array([1, 5, 9])
>>> a.transpose()
array([[ 0,  4,  8],
       [ 1,  5,  9],
       [ 2,  6, 10],
       [ 3,  7, 11]])
```

### 2.9.4 双向队列和其它形式的队列
> 利用`.append`和`.pop`方法，我们可以把列表当做栈或者队列来用。  
比如：`.appen`和`.pop(0)`合起来，就能模拟栈的**先进先出**的特点。

`collections.deque`类(双向队列)是一个线程安全、可以快速从两端添加或者删除元素的数据类型。
而且还可以指定长度,指定maxlen参数即可，一旦指定，不可修改。  
另外还有`from multiprocessing import Queue`，多进程通信就要用这个。

```
>>> from collections import deque
>>> dq = deque(range(5), maxlen=5)
>>> dq
deque([0, 1, 2, 3, 4], maxlen=5)
>>> dq.rotate(-4)
>>> dq
deque([4, 0, 1, 2, 3], maxlen=5)
>>> dq.append(9)
>>> dq
deque([0, 1, 2, 3, 9], maxlen=5)
>>> dq.pop()
9
>>> dq.pop()
3
>>> dq
deque([0, 1, 2], maxlen=5)
>>> dq.extend(['a','b',66])
>>> dq
deque([1, 2, 'a', 'b', 66], maxlen=5)
>>> dq.appendleft('xxx')
>>> dq
deque(['xxx', 1, 2, 'a', 'b'], maxlen=5)
>>> dq.extendleft([1, '2', 'dd'])
>>> dq
deque(['dd', '2', 1, 'xxx', 1], maxlen=5)
>>> dq.rotate(-4)
>>> dq
deque([1, 'dd', '2', 1, 'xxx'], maxlen=5)
```

#### deque.rotate
> 队列的旋转操作接受一个参数n，当`n > 0`时，队列的最右边的n个元素会被移动到队列的左边。  
当`n < 0`时，最左边的n个元素会被移动到最右边。注意n不是索引，而且元素的个数。

```
>>> dq.extend('12345')
>>> dq
deque(['1', '2', '3', '4', '5'], maxlen=5)
>>> dq.rotate(-4)
>>> dq
deque(['5', '1', '2', '3', '4'], maxlen=5)
>>> dq.extend('12345')
>>> dq
deque(['1', '2', '3', '4', '5'], maxlen=5)
>>> dq.rotate(4)
>>> dq
deque(['2', '3', '4', '5', '1'], maxlen=5)
```

`-4`的时候，把左边的`1,2,3,4`移动到最右边，那么`5`就到最左边了。  
`4`的时候，把右边的`2,3,4,5`4个元素移动到最左边，那么`1`就到最右边了。
