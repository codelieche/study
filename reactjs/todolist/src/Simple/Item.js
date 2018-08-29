/**
 * 代办事项Item
 */
import React, { Component } from "react";

class TodoItem extends Component {
    constructor(props){
        super(props);
        this.state = {
            data: this.props.data,
            finished: false,
        }
    }

    handleClick = () => {
        this.setState(prevState => {
            return {finished: ! prevState.finished}
        });
    }

    render(){
        var itemClass = this.state.finished ? "item finished" : "item";
        return (
            <div className={itemClass} onClick={this.handleClick}>
                {this.state.data}
            </div>
        );
    }
}

export default TodoItem;