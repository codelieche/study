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
