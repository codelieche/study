## 递归
> 递归（recursion），就是在运行的过程中调用自己。


### 斐波那契
> 斐波那契数列（Fibonacci sequence），又称黄金分割数列、因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）
以兔子繁殖为例子而引入，故又称为“兔子数列”.

斐波那契数列指的是这样一个数列 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233，377，610，987.......
这个数列从第3项开始，每一项都等于前两项之和。

斐波纳契数列以如下被以递归的方法定义：F(0)=0，F(1)=1, F(n)=F(n-1)+F(n-2)（n>=2，n∈N*）
在现代物理、准晶体结构、化学等领域，斐波纳契数列都有直接的应用，为此，美国数学会从1963年起出版了以
《斐波纳契数列季刊》为名的一份数学杂志，用于专门刊载这方面的研究成果。


递归和非递归方式将计算fibnacii的第N个值：

```python
def fibonacii(n):
    """
    用递归方法计算fibnacci
    :param n:
    :return:
    """
    if n < 0:
        return 0

    if n <= 2:
        return 1
    else:
        return fibonacii(n-1) + fibonacii(n-2)

def fibonacii_while(n):
    """
    用循环的方式计算斐波那契的值
    :param n:
    :return:
    """
    i, a, b = 0, 0, 1
    while i < n:
        a, b = b, a + b
        i = i + 1
    return a
```
