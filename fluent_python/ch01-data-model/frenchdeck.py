# -*- coding:utf-8 -*-

from collections import namedtuple


def demo_01():
    # nametuple simple demo
    User = namedtuple("User", ('name', 'age'))
    u1 = User("Jim", 20)
    u2 = User(name="Tom", age=26)
    print(u1.age, u1.name)
    print(u2.name, u2.age)
    print(u2[0], u2[1])

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
    return index_value


if __name__ == "__main__":
    # nametuple simple demo
    # demo_01()

    # French Card demo
    obj = FrenchDeck()
    print(len(obj))  # 52
    print(obj[27])  # Card(rank='8', suit='diamonds')
    print(obj[-1])  # Card(rank='A', suit='diamonds')
    # print(obj[55])  # IndexError: list index out of range

    # 对一系列牌进行排序
    # 根据card_spade_high含税对deck进行排序
    deck = FrenchDeck()
    for card in sorted(deck, key=card_spade_high):
        print(card)
