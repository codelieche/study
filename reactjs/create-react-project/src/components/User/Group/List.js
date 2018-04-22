/**
 * 用户分组 List
 */
import React from "react";
import _ from "lodash";
import { Link } from "react-router-dom";

import {
  Button,
  Breadcrumb,
  // Icon,
  Divider,
  Input,
  Popconfirm,
  Row,
  Col,
  Table,
  message
} from "antd";

export default class UserGroupList extends React.Component {
  constructor(props) {
    super(props);
    // 状态中dataSource是源数据【从服务器fetch过来的数组】
    // dataFilter是根据search输入框的变化而变化的【过滤查询后的数组】
    // 在删除操作中，删除了元素后，要修改dataSource和dataFilter的值【细节】
    this.state = {
      loaded: false,
      dataSource: [],
      dataFilter: []
    };
  }
  fetchData = () => {
    // 因为有个刷新按钮，防止连续点击
    // 当fetch完数据后设置loaded状态为true
    if (this.state.loaded) {
      this.setState({
        loaded: false
      });
    } else {
      //正在加载，如果dataSource不是空直接返回
      // 这个时候是因为点了刷新数据，但是上次刷新的请求正在进行中，有数据就直接返回吧
      if (this.state.dataSource.length > 0) {
        return;
      }
    }
    var url = "http://127.0.0.1:8080/api/v1/account/group/list";
    // 跨域访问默认是不带cookie的，这个特别注意
    fetch(url, { credentials: "include" })
      .then(response => response.json())
      .then(responseData => {
        // 返回的json数据是数组才去修改列表相关的数据
        if (responseData instanceof Array) {
          this.setState({
            dataSource: responseData,
            dataFilter: responseData,
            loaded: true
          });
        } else {
          this.setState({
            loaded: true
          });
          message.error(JSON.stringify(responseData), 5);
        }
      })
      .catch(err => {
        console.log(err);
        this.setState({
          loaded: true
        });
      });
  };
  componentDidMount() {
    this.fetchData();
  }

  deleteOnConfirm = value => {
    // console.log(value);
    // 开始删除
    const url = "http://127.0.0.1:8080/api/v1/account/group/" + value.id;
    fetch(url, { method: "DELETE", credentials: "include" })
      .then(response => {
        // 查看status状态码,ok(true/false)
        if (response.status === 204) {
          message.success("删除:" + value.name + "成功", 3);
          this.setState(prevState => {
            var prev_dataSource = prevState.dataSource;
            _.remove(prev_dataSource, value);
            // 删除元素后，修改状态
            return {
              dataSource: prev_dataSource,
              dataFilter: prev_dataSource
            };
          });
        } else {
          try {
            return response.json();
          } catch (error) {
            message.error("删除:" + value.name + "失败", 3);
          }
        }
      })
      .then(data => {
        if (data.message) {
          message.warn(data.message, 5);
        }
      })
      .catch(err => {
        console.log(err);
      });
  };

  deleteOnCancel = e => {
    // 选择取消的话，也弹出消息
    message.error("取消删除", 3);
  };

  onSearchHandler = value => {
    // 搜索框回车后处理函数
    // 主要就是使用lodash的filter从源数据是dataSource中过滤出dataFilter
    if (value) {
      var newData = [];
      var search = value.toLowerCase();
      newData = _.filter(this.state.dataSource, function (item) {
        return item.name.toLowerCase().indexOf(search) >= 0 || item.user_set
          ? item.user_set.join().indexOf(search) >= 0
          : false;
      });
      this.setState({
        dataFilter: newData
      });
    } else {
      // value是空了，表示不搜索了，那么就显示出全部数据
      this.setState(prevState => ({
        dataFilter: prevState.dataSource
      }));
    }
  };
  render() {
    // Table的列：Name、Parent、Type、Description、Action
    const columns = [
      {
        title: "ID",
        dataIndex: "id",
        key: "id",
        render: (text, record) => {
          return (
            <Link
              to={{
                pathname: "/user/group/" + record.id,
                state: { data: record }
              }}
            >
              {text}
            </Link>
          );
        },
        sorter: (a, b) => a.id - b.id
      },
      {
        title: "分组名",
        dataIndex: "name",
        key: "name"
      },
      {
        title: "用户",
        dataIndex: "user_set",
        key: "user_set",
        render: values => {
          return values.join(", ");
        }
      },
      {
        title: "操作",
        key: "action",
        // 使用自定义的render：三种操作按钮（Detail、Edior、Delete）
        render: (text, record) => {
          // console.log(text, record);
          return (
            <span>
              {/* Link传递数据，可以使用state，然后通过this.props.location.state来获取相应的数据 */}
              <Link
                to={{
                  pathname: "/user/group/" + text.id,
                  state: { data: text }
                }}
              >
                查看详情
              </Link>
              <Divider type="vertical" />
              <Link
                to={{
                  pathname: "/user/group/" + text.id + "/editor",
                  state: { data: text }
                }}
              >
                编辑
              </Link>
              <Divider type="vertical" />
              <Popconfirm
                title={"您确认删除:" + text.name + "?"}
                onCancel={this.deleteOnCancel}
                onConfirm={() => this.deleteOnConfirm(text)}
              >
                <a>删除</a>
              </Popconfirm>
            </span>
          );
        }
      }
    ];
    return (
      <div className="content">
        {/*面包屑开始  */}
        <Breadcrumb className="nav">
          <Breadcrumb.Item>
            <Link to="/">首页</Link>
          </Breadcrumb.Item>
          <Breadcrumb.Item>用户组</Breadcrumb.Item>
        </Breadcrumb>
        {/*面包屑 end  */}
        <div className="main">
          <div className="title">
            <h4>分组列表</h4>
          </div>
          {/*工具栏开始：搜索 刷新 添加  */}
          <Row className="tools">
            <Col span={12}>
              <Input.Search
                placeholder="search group"
                style={{ width: 200 }}
                onSearch={this.onSearchHandler}
              />
            </Col>
            <Col span={12} style={{ textAlign: "right" }}>
              <Button
                type="default"
                icon="reload"
                loading={!this.state.loaded}
                onClick={this.fetchData}
              >
                刷新
              </Button>
              <Link to="/user/group/add">
                <Button type="primary" icon="plus">
                  Add
                </Button>
              </Link>
            </Col>
          </Row>
          {/*工具栏 end  */}
          <Table
            columns={columns}
            dataSource={this.state.dataFilter}
            rowKey="id"
            bordered={true}
          />
        </div>
      </div>
    );
  }
}
