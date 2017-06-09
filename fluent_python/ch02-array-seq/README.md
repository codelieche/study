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
