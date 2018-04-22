/**
 * User相关的首页
 */
import React from "react";

import { Route, Switch, Redirect } from "react-router-dom";

// 导入User相关组件
// import UserLogin from './Login';
// 登陆不想使用默认的布局，所以在src/App.js顶级路由中就设置了，而不从src/Home.js中嵌入

import UserLogout from "./Logout";

// 用户相关的组件
import UserList from "./List";

// User Group相关的组件
import UserGroupList from "./Group/List";
import UserGroupAdd from "./Group/Add";
import UserGroupEditor from "./Group/Editor";
import UserGroupDetail from "./Group/Detail";

// User Message相关的组件
import UserMessage from './Message/Index';


class UserIndex extends React.Component {
    render() {
        return (
            <Switch>
                {/*用户相关的路由  */}
                {/* <Route exat path='/user/login' component={UserLogin} />  */}
                <Route exat path="/user/list" component={UserList} />
                <Route exat path="/user/logout" component={UserLogout} />

                {/*分组相关的路由  */}
                <Route exat path="/user/group/list" component={UserGroupList} />
                <Route exat path="/user/group/add" component={UserGroupAdd} />
                <Route exat path="/user/group/:id/editor" component={UserGroupEditor} />
                <Route exat path="/user/group/:id" component={UserGroupDetail} />
                <Route
                    exat
                    path="/user/group"
                    render={() => <Redirect to="/user/group/list" push={false} />}
                />

                {/*用户消息  */}
                <Route exat path="/user/message" component={UserMessage} />

                <Route
                    exat
                    path="/user"
                    render={() => <Redirect to="/user/list" push={false} />}
                />
            </Switch>
        );
    }
}

export default UserIndex;
