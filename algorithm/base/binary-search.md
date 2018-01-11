## 二分查找
> 二分查找是一种算法，其输入是一个有序的元素列表。  
如果要查找的元素包含在列表中，二分查找返回其位置，否则返回None。

### Python实现

```python
def binary_search(source_list, item):
    """
    二分查找
    :param source_list: 要查找的列表
    :param item: 要查找的元素
    :return: item的索引或者None
    """
    # 最小下标和最大下标
    low = 0
    high = len(source_list) - 1

    # 开始查找
    while low <= high:
        # 检查中间的元素
        mid = (low + high) // 2
        # 要检查的元素值
        guess = source_list[mid]
        if guess == item:
            return mid
        elif guess > item:
            # 猜的数字大了
            # 新的上界为： 中间值 - 1
            high = mid - 1
        else:
            # 猜的值小了
            # 新的下界从：中间值 + 1 开始
            low = mid + 1
    return None
```