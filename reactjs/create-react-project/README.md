# Create React Project

> 使用 react.js + ant.design

## 打包【结合 Djago 项目使用】

1. `yarn build`
2. 打开`main.xxx.js`把`http://127.0.0.1:8080/`替换成`/`
3. 把`mian.xxx.css` 和 `main.xxx.js`复制到后端代码的 static 相应 js 和 css 目录
4. 去后端代码的 templates 目录的`index.html`中替换掉`main.xxx.css`和`main.xxx.js`

## 基本使用

### 环境准备

* `Node.js`:[https://nodejs.org/](https://nodejs.org/)
* `npm`:
* `npx create-react-app create-react-project`: 创建项目
* `yarn`: `sudo npm install -g yarn`
* `create-react-app`:通过`sudo npm install -g create-react-app`安装【现在可以用 npx】

开发环境版本：

```
✗ node --version
v8.10.0
✗ npm --version
5.6.0
✗ create-react-app --version
1.5.2
```

### 基本命令

> 进入项目后，就可以执行命令了

* `yarn install`: 安装 package.json 中需要的包【请一定使用 yarn 安装】
* `yarn start`: 启动项目，默认启动服务：`http://localhost:3000/`（端口被占用，会+1）
* `npm run build`或者`yarn run build`: 创建打包后的 js 代码文件，文件位置：`./build`中
* `build`中注意，其中的配置:`config/webpack.config.prod.js`

#### 温馨提示

1. 随着时间的推移，你可能想用更新的 react.js 了，而你可以先自己创建个项目，然后直接把老项目中的 src 目录复制过去即可
2. 同时注意要设置 Ant Design 按需加载，需要`yarn run eject`后，需要修改配置【dev 和 prod 的都需要修改哦！！！】，请参考相关文档
3. 同时还有依赖库，直接 copy src 目录后，特别还要注意这个问题

### 依赖库

> package.json 中列出了太多，很多都是 create-react-app 创建的时候添加的。具体的版本好，可以去 package.json 文件中查看，想更新最新的，也都是 OK 的。而重点的库列表如下：

#### dependencies

* `react`
* `react-dom`
* `react-router-dom`: react 路由相关
* `antd`: UI 库

#### devDependencies

* `babel-plugin-import`: antd 按需引用要用到
* `react-app-rewire-less`: 处理 less 文件
* `react-app-rewired`: 默认配置进行自定义会用到
