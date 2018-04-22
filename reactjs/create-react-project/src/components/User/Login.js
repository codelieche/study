/**
 * 用户登陆组件
 */
import React, { Component } from "react";
import { Layout, Row, Col, Form, Icon, Input, Button, message } from "antd";

import URLSearchParams from "../Utils/UrlParam";
import logo from '../../asset/images/logo.svg';

const FormItem = Form.Item;

class LoginForm extends Component {
    handleSubmit = e => {
        e.preventDefault();
        this.props.form.validateFields((err, values) => {
            if (!err) {
                // POST登陆账号
                const url = "http://127.0.0.1:8080/api/v1/account/login";
                // 跨域默认是不传递cookie的，要传递cookies需要设置credential: include
                fetch(url, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        Accept: "application/json"
                    },
                    body: JSON.stringify(values),
                    credentials: "include"
                })
                    .then(response => response.json())
                    .then(data => {
                        // console.log(data);
                        if (data.status === "success" || data.status === true) {
                            // 获取next的url
                            // 首先获取search参数：?next=/
                            const params = new URLSearchParams(this.props.location.search);
                            // 获取next的值
                            let next = params.get("next");
                            // 如果next为null或者next为/user/login那么就跳转到首页
                            if (!next || next === "/user/login") {
                                next = "/";
                            }
                            // 跳转去首页
                            // console.log('即将跳转', next);
                            // this.props.history.push(next);
                            var url = window.location.origin + next;
                            window.location.href = url;
                        } else {
                            message.error("登陆失败:" + data.message, 5);
                        }
                    })
                    .catch(err => {
                        console.log(err);
                    });
            } else {
                console.log(err);
                message.error("登陆失败，请重新登陆", 3);
            }
        });
    };

    componentWillMount() {
        try {
            localStorage.reFreshPathname = null;
        } catch (error) { }
    }

    render() {
        const { getFieldDecorator } = this.props.form;
        return (
            <Layout style={{ height: "100vh" }}>
                <Row style={{ height: "100vh" }}>
                    <Col xs={{ span: 20, offset: 2 }} lg={{ span: 6, offset: 9 }} className="user-login">
                        <div
                            className="logo"
                            style={{ textAlign: "center" }}
                        >
                            <img
                                src={logo}
                                alt="Logo"
                            />
                        </div>

                        <Form onSubmit={this.handleSubmit} className="login-form">
                            <FormItem>
                                {getFieldDecorator("username", {
                                    rules: [{ requirend: true, message: "请输入用户名" }]
                                })(
                                    <Input
                                        prefix={<Icon type="user" style={{ fontSize: 16 }} />}
                                        placeholder="username"
                                    />
                                )}
                            </FormItem>

                            <FormItem>
                                {getFieldDecorator("password", {
                                    rules: [{ required: true, message: "请输入密码" }]
                                })(
                                    <Input
                                        prefix={<Icon type="lock" style={{ fontSize: 16 }} />}
                                        size="large"
                                        type="password"
                                        placeholder="password"
                                    />
                                )}
                            </FormItem>

                            <FormItem className="login">
                                <Button
                                    type="primary"
                                    htmlType="submit"
                                    className="login-form-button"
                                    style={{ width: "100%" }}
                                >
                                    Login in
                                </Button>
                            </FormItem>
                            <FormItem className="footer">
                                <Row>
                                    <Col span={12} className="login-form-change">
                                        <a>修改密码</a>
                                    </Col>
                                    <Col span={12} className="login-form-forget">
                                        <a>忘记密码</a>
                                    </Col>
                                </Row>
                            </FormItem>
                        </Form>
                    </Col>
                </Row>
            </Layout>
        );
    }
}

var Login = Form.create()(LoginForm);
export default Login;
