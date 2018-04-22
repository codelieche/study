/**
 * 用户组 添加 页
 */
import React from "react";
import { Link } from "react-router-dom";

import { Breadcrumb, message } from "antd";

import UserGroupForm from "./Form";

export default class ProjectAdd extends React.Component {
  // constructor(props) {
  // super(props);
  // }
  componentDidMount() { }

  handleAddSubmit = values => {
    // console.log(values);
    // 通过fetch POST添加Group
    const url = "http://127.0.0.1:8080/api/v1/account/group/create";
    fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json"
      },
      credentials: "include",
      body: JSON.stringify(values)
    })
      .then(response => response.json())
      .then(data => {
        // console.log(data);
        if (data.id > 0) {
          // 当data中有id字段，就表示添加成功了，跳转去group的详情页
          this.props.history.push("/user/group/" + data.id);
        } else {
          message.error(JSON.stringify(data), 8);
        }
      })
      .catch(err => {
        console.log(err);
      });
  };

  render() {
    return (
      <div className="content">
        <Breadcrumb className="nav">
          <Breadcrumb.Item>
            <Link to="/">首页</Link>
          </Breadcrumb.Item>
          <Breadcrumb.Item>
            <Link to="/user/group">用户组</Link>
          </Breadcrumb.Item>
          <Breadcrumb.Item>添加</Breadcrumb.Item>
        </Breadcrumb>
        <div className="main">
          <div className="title">
            <h4>添加用户组</h4>
          </div>
          <div className="wrap">
            <UserGroupForm handleSubmit={this.handleAddSubmit} />
          </div>
        </div>
      </div>
    );
  }
}
