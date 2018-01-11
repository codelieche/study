## 大O表示法
> 大O表示法是一种特殊的表示法，指出了算法的速度有多快。  
大O表示法让你能够比较操作数，它指出了算法运行时间的增速。


**例如：**假设列表包含`n`个元素，简单查找需要检查每个元素，因此需要执行`n`次操作。  
使用大O表示法，这个运行时间为`O(n)`。

大O表示法指出了最糟情况下的运行时间(步骤),`O(n)`与`O(log n)`

### 一些常见的大O运行时间
- `O(n)`: 线性时间，这样的算法包括简单查找
- `O(log n)`: 对数时间，这样的算法包括二分查找
- `O(n * log n)`: 这种算法包括，快速排序
- `O(n平方)`: O(n2)，这种算法包括，选择排序
- `O(n!)`: 比如一些旅行商问题的解决方案（旅行5个城市，确保旅程最短），一种非常慢的算法

### 关于大O表示法
- 二分查找的速度比简单查找快很多
- `O(log n)`比`O(n)`快，需要搜索的元素越多，前者比后者就快得越多
- 算法运行时间并不以秒为单位
- 算法运行时间是从其增速的角度度量的
- 算法运行时间用大O表示法表示
