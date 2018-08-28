/**
 * 简单版本的TodoList
 */
import React, { Component } from "react";

import TodoItem from "./Item";
import "../Styles/simple.css";

class SimpleTodoList extends Component {
    constructor(props){
        super(props);
        this.state = {
            // 输入框的值
            inputValue: "",
            // Todo List的列表数据
            dataList: [],
        }
    }

    handlerInputeChange = (e) => {
        var value = e.target.value;
        this.setState({inputValue: value})
    }

    handlerButtonSubbmit = () => {
        // 当按钮提交的时候
        this.setState(prevState => {
            let currentItemData = prevState.inputValue;
            let newDataList = [...prevState.dataList, currentItemData];
            return {
                inputValue: "",
                dataList: newDataList,
            }
        });
    }

    render(){
        var todoItems;
        if(this.state.dataList.length > 0){
            todoItems = this.state.dataList.map((item, index) => {
                return <TodoItem data={item} key={index} />;
            });
        }else{
            todoItems = <div className="no-items">无代办事项</div>;
        }
        

        return (
            <div className="container todolist">
                <div className="header">
                    <input placeholder="代办事项"
                      value={this.state.inputValue}
                      onChange={this.handlerInputeChange} />
                    <button type="subbmit" onClick={this.handlerButtonSubbmit}>提交</button>
                </div>
                <div className="list">
                    {todoItems}
                </div>
            </div>
        );
    }
    
}

export default SimpleTodoList;