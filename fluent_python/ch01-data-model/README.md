# 第一章：数据模型

## 1.1：一摞Python风格的纸牌
### nametuple
> 当我们使用元组`user = ("Jim", 20)`获取名字使用`user[0]`,年龄`user[1]`。
虽然这样获取属性也ok，但是0、1还是不够语义化，我们想通过`user.age`，`user.name`获取年龄和名字的属性。
我们自定义个类，有时候我们只想有属性没方法的简单类，这时候`nametuple`就满足需求。

#### 示例

```python
from collections import namedtuple
User = namedtuple("User", ('name', 'age'))
u1 = User("Jim", 20)
u2 = User(name="Tom", age=26)
print(u1.age, u1.name)
print(u2.name, u2.age)
print(u2[0], u2[1])
```

结果：

```
(20, 'Jim')
('Tom', 26)
('Tom', 26)
```

### FrenchDeck

```python

from collections import nametuple

# 定义命名元组类：Card
# Card有两个属性，一个是花色，一个是数值大小
Card = namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    # 扑克牌类
    # rank: 1-10 JKQA, suit：黑红方梅（spades, hearts, clubs, diamonds）
    ranks = [str(i) for i in range(2, 11)] + list("JKQA")
    suits = "spades hearts clubs diamonds".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                       for suit in self.suits]

    def __len__(self):
        # 返回所有牌的长度
        # 使用len(obj)返回长度
        return len(self._cards)

    def __getitem__(self, position):
        # 根据序号返回对应的扑克牌
        # 使用obj[n] 返回对应的扑克牌
        # n可以是正数也可以上负数，但是不能超出len-1
        return self._cards[position]
```

#### 随机选取一个

```
>>> from frenchdeck import FrenchDeck
>>> from random import choice
>>> deck = FrenchDeck()
>>> choice(deck)
Card(rank='J', suit='diamonds')
```

#### 随机选取N个

```
>>> from random import sample
>>> sample(deck, 3)
[Card(rank='3', suit='spades'), Card(rank='Q', suit='spades'), Card(rank='2', suit='clubs')]
```

#### __getitem__
> 因为FrenchDeck类中的`__getItem__`方法把`[]`操作交给了了`self._cards`列表，所以我们deck自动支持切片(slice)操作。

```
>>> deck[:3]
[Card(rank='2', suit='spades'), Card(rank='2', suit='hearts'), Card(rank='2', suit='clubs')]
>>> deck[12::20]
[Card(rank='5', suit='spades'), Card(rank='10', suit='spades')]

```

> 另外仅仅实现了`__getitem__`方法，这一系列牌就变成可迭代的了。

```
>>> for card in deck:
...     print(card)
... 
Card(rank='2', suit='spades')
Card(rank='2', suit='hearts')
Card(rank='2', suit='clubs')
...
```

反向迭代：

```
>>> for card in reversed(deck):
...     print(card)
...
Card(rank='A', suit='diamonds')
Card(rank='A', suit='clubs')
Card(rank='A', suit='hearts')
...
```

#### 对扑克牌进行排序
> 利用python内置函数sorted,我们对每个牌，根据其序号和花色，算出了值，根据这个值来排序。

```python

# 根据黑红梅方排序，由大到小
suite_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

# 定义复合序号算法
def card_spade_high(card):
    # 相同数值的拍，黑色最大
    # 先获取rank的索引序号
    # [2, 3, 4, 5, 6, 7, 8.... J, K, Q, A]
    rank_value = FrenchDeck.ranks.index(card.rank)
    # 每个大小的牌有4个花色，那么复合序号就是，4 * n + 花色序号value
    index_value = rank_value * len(suite_values) + suite_values[card.suit]

# 根据card_spade_high函数对deck进行排序
deck = FrenchDeck()
for card in sorted(deck, key=card_spade_high):
    print(card) 
```

----

## 1.2：如何使用特殊方法

### 1.2.1: 一个简单的二维向量
> Vector的`+`、`-`、`*`、`abs`等方法是用特殊方法实现的：`__repr__`、`__abs__`、`__add__`和`__mul__`。

```python

from math import hypot
# hypot 是求三角形的斜边长

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        # obj显示的会是 Vector(x, y)，而不是<Vector instance at 0x107b9b3f8>
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
```

测试：

```
>>> from vector import Vector
>>> v1 = Vector(5, 6)
>>> v2 = Vector(3, 4)
>>> v1 + v2
Vector(8, 10)
>>> v1 * 4
Vector(20, 24)
>>> abs(v1)
7.810249675906654
>>> abs(v2)
5.0
>>> print(v1)
Vector(5, 6)
```

### 1.2.2 字符串表示形式
> 内置函数`repr`,能把一个对象用字符串的形式表达出来以便辨认，这就是**字符串表示形式**。
 `repr`是用`__repr__`方法实现的。

`__repr__`和`__str__`的区别：
`__str__`是在`str()`函数被使用，或是在`print`函数打印一个对象的时候才被调用，
并且它返回的字符串对终端用户更友好。如果2个中实现一个，推荐`__repr__`。没有`__str__`会用`__repr__`代替。

### 1.2.3 算数运算符
> `__add__`和`__mul__`，可以对前面的`Vector`带来`+`和`*`这两个算数运算符。

### 1.2.4 自定义布尔值
> `if`, `while`语句，或者`and`、`or`和`not`运算符。为了判定一个值`x`是真还是假，
Python会调用`bool(x)`，这个函数只能返回`True`或者`False`。
`bool(x)`的背后是调用`x.__bool__()`的结果，如果不存在`__bool__`方法，那么`bool(x)`会尝试调用`x.__len__()`。
若返回0，则bool会返回False; 否则返回True。
默认情况下，我们自定义的类的实例总是返回真的，除非我们自己实现了`__bool__`或者`__len__`方法。

## 1.3：特殊方法一览

### 跟运算符无关的特殊方法

类名  |   方法名
----  |  ----
字符串/字节序列表示形式    |   `__repr__、__str__、__format__、__bytes__`
数值转换    |   `__abs__、__bool__、__complex__、__int__、__float__、__hash__、__index__`
集合模拟    |   `__len__、__getitem__、__setitem__、__delitem__、__contains__`
迭代枚举    |   `__iter__、__reversed__、__next__`
可调用模拟   |   `__call__`
上下文管理器  |   `__enter__、__exit__`
实例创建和销毁 |   `__new__、__init__、__del__`
属性管理器   |   `__getattr__、__getattribute__、__setattr__、__delattr__、__dir__`
属性描述符   |   `__get__、__set__、__delete__`
跟类相关的服务 |   `__prepare__、__instancecheck__、__subclasscheck__`

### 跟运算符相关的特殊方法

类名  |   方法名和对应的运算符
----  |  ----
一元运算符   |   `__neg__ - 、__pos__ + 、__abs__ abs()`
众多比较运算符 |   `__lt__ <、__le__ <= 、__eq__ == 、__gt__ > 、__ge__ >=`
算术运算符   |   `__add__ + 、__sub__ - 、__mul__ * 、__truediv__ / 、__floordiv__ // 、__mod__ % 、__divmod__ divmod() 、__pow__ **或pow() 、__round__ round()`
反向算术运算符 |   `__radd__、__rsub__、__rmul__、__rtrudiv__、__rfloordiv__、__rmod__、__rdivmod__`
增量赋值算术运算符   |   `__iadd__、__isub__、__imul__、__itruediv__、__ifloordiv__、__imod__、__ipow__`
位运算符    |   `__invert__ ~ 、__lshift__ << 、__rshift__ >> 、__and__ & 、__or__ | 、 __xor__ ^`
反向位运算符   |   `__rlshift__、__rrshift__、__rand__、__rxor__、__row__`
增量赋值位运算符    |   `__ilshift__、__irshift__、__iand__、__ixor__、__ior__`
