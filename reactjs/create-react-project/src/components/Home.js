import React, { Component } from 'react';

import {
    Layout,
    Icon,
} from 'antd';
// import {
//     // BrowserRouter as Router,
//     Switch,
//     Route,
// } from 'react-router-dom';

import Header from './Base/Header';
import Nav from './Base/Nav';
import Footer from './Base/Footer';

// 检查登陆的方法
import CheckLogined from "./Utils/auth";


const { Sider, Content } = Layout;

export default class Home extends Component {
    constructor(props) {
        super(props);
        this.state = {
            collapsed: false,
            laskCheckTime: new Date()
        };
        // console.log(this.props.location);
    }

    componentDidMount() {
        // 组件将要mount前先检查下用户是否登陆了
        if (this.props.history.action === "PUSH") {
            // 不需要检查是否登陆
        } else {
            // 为了测试，只要不是/的就都检查
            if (this.props.location.pathname !== "/") {
                CheckLogined(this.props);
            }
        }
    }

    static getDerivedStateFromProps(nextProps, prevState) {
        if (nextProps.history.action === "PUSH") {
            // 每次点击了新的页面检查登陆
            var now = new Date();
            var sub = 0;
            sub = now.getTime() - prevState.laskCheckTime.getTime();
            // 六分钟之内不检查是否登陆
            if (sub > 1000 * 60 * 6) {
                // CheckLogined需要三个参数：{ history, match, location }
                CheckLogined(nextProps);
                return {
                    laskCheckTime: now,
                }
            } else {
                // console.log("不需要检查登陆", sub);
            }
        }
        return null;
    }

    toggle = () => {
        // Nav缩放开关
        this.setState(prevState => ({
            collapsed: !prevState.collapsed,
            defaultOpenKey: this.props.defaultOpenKey ? this.props.defaultOpenKey : null,
        }));
    }

    onCollapse = (collapsed) => {
        // Sider的onCollapse事件
        this.setState({ collapsed });
    }

    checkLoginOperation = () => {
        var now = new Date();
        var sub = 0;
        sub = now.getTime - this.state.laskCheckTime.getTime();
        // 六分钟之内不检查是否登陆
        if (sub > 1000 * 600) {
            this.setState({ laskCheckTime: now });
            CheckLogined(this.props);
        } else {
            // console.log("不需要检查登陆", sub);
        }
    };

    render() {
        return (
            <Layout style={{ height: '100vh', overflow: 'auto' }}>
                {/* 头部内容开始 */}
                <Layout.Header className="header">
                    <Header />
                </Layout.Header>
                {/* 头部内容 end */}

                {/* header下面主体内容开始 */}
                <Layout>
                    {/* 左侧侧边栏 */}
                    <Sider
                        trigger={null}
                        collapsible
                        collapsed={this.state.collapsed}
                        onCollapse={this.onCollapse}
                        className="sider"
                        collapsedWidth={65}
                        breakpoint="sm"
                    >
                        <div onClick={this.toggle.bind(this)} className="sider-toggle">
                            <Icon type={this.state.collapsed ? "menu-unfold" : "menu-fold"} />
                        </div>
                        <Nav collapsed={this.state.collapsed}
                            defaultOpenKey={this.props.defaultOpenKey}
                            pathname={this.props.location.pathname} />
                    </Sider>
                    {/* 左侧侧边栏 end */}

                    {/* 右侧主体内容开始 */}
                    <Layout style={{ maxHeight: '100vh', overflow: 'auto' }}>

                        {/* 主体内容开始 */}
                        <Content className="container">
                            {this.props.history.location.pathname}
                        </Content>
                        {/* 主体内容end */}

                        {/* 右侧底部内容开始 */}
                        <Layout.Footer>
                            <Footer />
                        </Layout.Footer>
                        {/* 右侧底部内容 end */}

                    </Layout>
                    {/* 右侧主体内容 end */}

                </Layout>
            </Layout>
        );
    }
}