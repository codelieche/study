/**
 * 用户编辑表单
 * 需要传递的属性(props):
 * 1. data: 从列表页传递过来用户的data信息
 * 2. handleSubmit: 表单提交的操作
 *     a. 需要传递url：编辑用户的url
 *     b. 需要传递values：表单数据
 */
import React, { Component } from "react";

import { Row, Col, Button, Form, Input, Radio } from "antd";

function hasErrors(fieldsError) {
    // console.log(fieldsError);
    // console.log(Object.keys(fieldsError).some(field => fieldsError[field]));
    return Object.keys(fieldsError).some(field => fieldsError[field]);
}

class FormBase extends Component {
    constructor(props) {
        super(props);
        var data = this.props.data ? this.props.data : {};
        this.state = {
            data: data
        };
    }

    static getDerivedStateFromProps(nextProps, prevState) {
        // 父组件传递了新的data过来，需要更新下
        if (nextProps.data !== prevState.data) {
            var data = nextProps.data;
            // 更新表单值
            if (data.id > 0) {
                nextProps.form.setFieldsValue({
                    nick_name: data.nick_name,
                    is_active: data.is_active,
                    is_superuser: data.is_superuser,
                    mobile: data.mobile,
                    dingding: data.dingding,
                    wechart: data.wechart
                });
            }

            return {
                data: data
            };
        } else {
            return null
        }
    }

    handleSubmit = e => {
        // 提交表单的处理函数
        // Form表单实例化的时候传递了handleSubmit，实际的操作都是调用它的
        // 主要是：editor或add操作

        e.preventDefault();
        this.props.form.validateFields((err, values) => {
            if (!err) {
                // var url = `http://127.0.0.1:8080/api/1.0/account/user/${this.state.data.id}`;
                this.props.handleSubmit(values);
            }
        });
    };

    render() {
        const { getFieldDecorator, getFieldsError } = this.props.form;

        // 左侧表单Item的布局设置
        const formItemLayout = {
            labelCol: {
                xs: { span: 8 },
                sm: { span: 8 },
                md: { span: 8 }
            },
            wrapperCol: {
                xs: { span: 12 },
                sm: { span: 12 },
                md: { span: 12 }
            }
        };
        // 表单尾部的布局样式：Button
        const tailFormItemLayout = {
            wrapperCol: {
                xs: {
                    span: 8,
                    offset: 8
                },
                sm: {
                    span: 8,
                    offset: 10
                }
            }
        };

        return (
            <Form onSubmit={this.handleSubmit}>
                <Row>
                    <Col xs={24} sm={24}>
                        <Form.Item {...formItemLayout} label="用户名">
                            {getFieldDecorator("username", {
                                initialValue: this.state.data.username
                            })(<Input placeholder="用户名" disabled={true} />)}
                        </Form.Item>
                        <Form.Item {...formItemLayout} label="昵称">
                            {getFieldDecorator("nick_name", {
                                initialValue: this.state.data.nick_name
                            })(<Input placeholder="昵称" />)}
                        </Form.Item>
                        <Form.Item
                            {...formItemLayout}
                            label="状态"
                            help="这里设置禁用不会删除用户代码和数据库权限"
                        >
                            {getFieldDecorator("is_active", {
                                initialValue: this.state.data.is_active,
                                rules: [{ required: true, message: "请选择是否开启用户!" }]
                            })(
                                <Radio.Group size="small">
                                    <Radio.Button value={true}>开启</Radio.Button>
                                    <Radio.Button value={false}>禁用</Radio.Button>
                                </Radio.Group>
                            )}
                        </Form.Item>

                        <Form.Item {...formItemLayout} label="超级用户">
                            {getFieldDecorator("is_superuser", {
                                initialValue: this.state.data.is_superuser,
                                rules: [{ required: true, message: "请选择是否是超级用户!" }]
                            })(
                                <Radio.Group size="small">
                                    <Radio.Button value={true}>是</Radio.Button>
                                    <Radio.Button value={false}>否</Radio.Button>
                                </Radio.Group>
                            )}
                        </Form.Item>

                        <Form.Item {...formItemLayout} label="手机号">
                            {getFieldDecorator("mobile", {
                                initialValue: this.state.data.mobile,
                                rules: [{ required: false, message: "请输入手机号!", max: 20 }]
                            })(<Input placeholder="mobile" />)}
                        </Form.Item>

                        <Form.Item {...formItemLayout} label="钉钉ID">
                            {getFieldDecorator("dingding", {
                                initialValue: this.state.data.dingding
                            })(<Input placeholder="dingding" />)}
                        </Form.Item>

                        <Form.Item {...formItemLayout} label="微信ID">
                            {getFieldDecorator("wechart", {
                                initialValue: this.state.data.wechart
                            })(<Input placeholder="wechart" />)}
                        </Form.Item>
                    </Col>
                    <Col xs={24} sm={24} md={12} />
                </Row>
                <Form.Item {...tailFormItemLayout}>
                    <Button
                        type="primary"
                        htmlType="submit"
                        disabled={hasErrors(getFieldsError())}
                    >
                        修改
          </Button>
                </Form.Item>
            </Form>
        );
    }
}

export default Form.create()(FormBase);
