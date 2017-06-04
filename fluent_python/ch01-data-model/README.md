## 第一章：数据模型

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

# 根据card_spade_high含税对deck进行排序
deck = FrenchDeck()
for card in sorted(deck, key=card_spade_high):
    print(card) 
```
    