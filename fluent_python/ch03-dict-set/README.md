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

## 3.2 字典推导

```
>>> l = [('two', 2), ('three', 3), ('one', 1)]
>>> d = {v: k for k,v in l} 
>>> d
{2: 'two', 3: 'three', 1: 'one'}
>>> {k: v.upper() for k,v in d.items() if k >= 2}
{2: 'TWO', 3: 'THREE'}
```

## 3.3 常见的映射方法
在`collections`中还有`defaultdict`和`OrderedDict`。


## 3.4 映射的弹性键查询
> 有时候为了方便起见，就算某个键在映射里不存在，我们也希望在通过这个键读取值的时候能得到一个默认值。

有两种方式：  
1. 通过`collections.defaultdict`这个类,而不是`dict`
2. 自己定义一个`dict`的子类，然后在子类中实现`__missing__`方法

### 3.4.1：defaultdict 处理找不到的键的一个选择
> 把内置函数`list`传给defaultdict.

```
>>> from collections import defaultdict
>>> dd = defaultdict(list)
>>> dd['gg']
[]
>>> dd
defaultdict(<class 'list'>, {'gg': []})
>>> dd['ff']
[]
>>> dd
defaultdict(<class 'list'>, {'gg': [], 'ff': []})
>>> dd.items()
dict_items([('gg', []), ('ff', [])])
```

> 自定义个函数传给`defaultdict`
 
```
 >>> def fun():
...     return 1
... 
>>> dd2 = defaultdict(fun)
>>> dd2['a']
1
>>> dd2['a'] += 1
>>> dd2['b']
1
>>> dd2
defaultdict(<function fun at 0x106d33f28>, {'a': 2, 'b': 1})
>>> dd2.items()
dict_items([('a', 2), ('b', 1)])
```

### 3.4.2：特殊方法 __missing__
> 所有的映射类型在处理找不到的键的时候，都会牵扯到`__missing__`方法。  
自定义dict子类，实现`__missing__`方法，那么在`__getitem__`碰到找不到键的时候，
python就会自动调用它，而不是抛出一个`KeyError`异常。

**注意：**  
`__missing__`方法只会被`__getitem__`触发(比如：在表达式d[k]）  
 而`__missing__`方法对`get`或者`__contains__`(in运算符会用到这个特殊方法)无影响。
 
 ```
 >>> dd2
defaultdict(<function fun at 0x106d33f28>, {'a': 2, 'b': 1})
>>> dd2['c']
1
>>> dd2.get('d')
>>> dd2.get('c')
1
>>> 'd' in dd2
False
```


