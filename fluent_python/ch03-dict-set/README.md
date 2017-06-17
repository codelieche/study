# 第3章：字典和集合

## 3.1 泛映射类型
> `collections.abc`模块中有`Mapping`和`MutableMapping`这两个抽象基类，
他们的作用是为`dict`和其它类似的类型定义像是接口。

```
>>> d = {}
>>> isinstance(d, abc.Mapping)
True
>>> isinstance(d, abc.MutableMapping)
True
>>> type(d)
<class 'dict'>
```

### 可散列的数据类型
> 如果一个对象是可散列的，那么在这个对象的生命周期中，它的散列值是不便的，
而且这个对象需要实现`__hash__()`方法。  
另外可散列对象还要有`__qe__()`方法，这样才能跟其它建做比较。
如果两个可散列对象是相等的，那么它们的散列值一定是一样的。

原子不可变数据类型（`str`,`bytes`和数值类型）都是可散列类型，frozenset也是可散列类型。  
元组的话，当所有元素都是可散列类型时，它才是可散列的。

```
>>> t1 = (1, 2, 3, (4, 'abc'))
>>> hash(t1)
6414027367281304396
>>> t2 = (1, 2, 3, [4, 'abc'])
>>> hash(t2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> t3 = (1, 2, 3, frozenset([4, 'abc']))
>>> hash(t3)
7991449080708116453
```

```
>>> d1 = dict(one=1, two=2, three=3)
>>> d2 ={'one':1, 'two':2, 'three':3}
>>> d3 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
>>> d4 = dict([('two', 2), ('three', 3), ('one', 1)])
>>> d5 = dict({'three': 3, 'two': 2, 'one': 1})
>>> d1 == d2 == d3 == d4 == d5
True
>>> d1 is d2
False
>>> d2 is d3
False
```
> Dict有多张构造方法，上面的示例，虽然的`d1 == d2 == d3 == d4 == d5`，但是它们的id是不同的哦。

