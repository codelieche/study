# React.js Tutorial: Tic-Tac-Toe

## 参考文档
- [reactjs.org](https://reactjs.org/)
- [tutorial](https://reactjs.org/tutorial/tutorial.html)



## 技术点

### 对象的改变
**1. Data change with mutation**

```js
var player = {score: 1, name: 'Jeff'};
player.score = 2;
// Now player is {score: 2, name: 'Jeff'}
```

**2. Data change without mutation**
> 有时候我们想在player的基础上修改数据，但是不想让原对象也跟着改变了，或者说想深拷贝一下。

```js
var player = {score: 1, name: 'Jeff'};

var newPlayer = Object.assign({}, player, {score: 2});
// Now player is unchanged, but newPlayer is {score: 2, name: 'Jeff'}

// Or if you are using object spread syntax proposal, you can write:
// var newPlayer = {...player, score: 2};
```
