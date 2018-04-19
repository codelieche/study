import React from 'react';

import {
    Layout,
    Icon,
} from 'antd';
import Header from './Base/Header';
import Nav from './Base/Nav';
import Footer from './Base/Footer';

// 导入测试组件


const { Sider, Content } = Layout;


export default class TestHome extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            collapsed: false,
            showLoading: false
        };

    }
    toggle = () => {
        this.setState({
            collapsed: !this.state.collapsed,
            defaultOpenKeys: [],
        });
    }
    onCollapse = (collapsed) => {
        this.setState({ collapsed });
    }

    showLoadingFun = () => {
        console.log(this.state.showLoading);
        if (this.state.showLoading) {
            this.setState(
                {
                    showLoading: false
                }, this.showLoadingFun
            );
        } else {
            this.setState({ showLoading: true });
        }

    }
    render() {
        return (
            <Layout style={{ height: '100vh', overflow: "auto" }}>
                <Layout.Header className="header">
                    <Header />
                </Layout.Header>
                <Layout>
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
                            <Icon type={this.state.collapsed ? "menu-unfold" : "menu-fold"} style={{}} />
                        </div>
                        <Nav collapsed={this.state.collapsed} defaultOpenKey={this.props.defaultOpenKey} />
                    </Sider>
                    <Layout style={{ maxHeight: '100vh', overflow: 'auto' }}>
                        <Content className="container">

                            {/* 测试颜色 */}
                            <div style={{ padding: "10px", textAlign: "center", color: "#fff", verticalAlign: "middle", lineHeight: "50px" }}>
                                <div style={{ marginTop: 20, height: '150px', background: '#00c1de' }}>#00c1de</div>
                                <div style={{ marginTop: 20, height: '50px', background: '#373d41' }}>#373d41</div>
                                <div style={{ marginTop: 20, height: '50px', background: '#42485B' }}>#42485B</div>
                                <div style={{ marginTop: 20, height: '50px', background: '#333744' }}>#333744</div>
                                <div style={{ marginTop: 20, height: '50px', background: '#333' }}>#333</div>
                                <div style={{ marginTop: 20, height: '50px', background: '#00c1de' }}>#00c1de</div>
                            </div>

                        </Content>
                        <Layout.Footer>
                            <Footer />
                        </Layout.Footer>
                    </Layout>
                </Layout>
            </Layout>
        );
    }
}