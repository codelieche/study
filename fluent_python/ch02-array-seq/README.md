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
