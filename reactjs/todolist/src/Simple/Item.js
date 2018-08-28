/**
 * 代办事项Item
 */
import React, { Component } from "react";

class TodoItem extends Component {
    constructor(props){
        super(props);
        this.state = {
            data: this.props.data,
        }
    }

    render(){
        return (
            <div className="item">
                {this.state.data}
            </div>
        );
    }
}

export default TodoItem;