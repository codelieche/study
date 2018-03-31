## MRO

> MRO(Method Resolution Order): 方法解析顺序。

### 菱形继承

- 类D
- B和C继承了D
- A继承了B和C

```python
class D:
    pass

class C(D):
    pass

class B(D):
    pass

class A(B, C):
    pass

print(A.mro())
print(A.__mro__)
```

输出的结果：

```
[<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>]
(<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>)
```

查找顺序，先去A，然后去B，再去C，最后再去D，最后就是object。  
object是所有类的基类。


### 再来一个示例

- 两个父类，D和E
- B和C分别继承D，E
- 最后A继承了B和C

```python
class E:
    pass

class D:
    pass

class B(D):
    pass

class C(E):
    pass

class A(B, C):
    pass

print(A.mro())
print(A.__mro__)
```

输出的结果：

```
[<class '__main__.A'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.C'>, <class '__main__.E'>, <class 'object'>]
(<class '__main__.A'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.C'>, <class '__main__.E'>, <class 'object'>)
```

查找顺序：`A` --> `B` --> `D --> `C` --> `E` --> `object`


