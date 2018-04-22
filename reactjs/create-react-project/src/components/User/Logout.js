/**
 * 用户退出登录，然后跳转到登录页
 */

import React from "react";

import { Redirect } from "react-router-dom";

import { message } from "antd";

export default class Logout extends React.Component {
    componentDidMount() {
        this.logout();
    }

    logout = () => {
        const url = "http://127.0.0.1:8080/api/v1/account/logout";
        fetch(url, { method: "GET", credentials: "include" })
            .then(response => response.json())
            .then(data => {
                //  console.log(data);
                if (data.status) {
                    message.success("退出登录成功");
                }
            })
            .catch(err => {
                console.log(err);
            });
    };

    render() {
        return <Redirect to="/user/login" push={false} />;
    }
}
