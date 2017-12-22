/**
 * 棋盘正方形组件
 */
import React from 'react';

class Square extends React.Component {
    // 棋盘中的正方形
    constructor(props) {
        super(props);
        this.state = {
            value: null,
        };
    }

    render() {
        return (
        <button className="square" onClick={this.props.onClick}>
            {this.props.value}
        </button>
        );
    }
}

export default Square;
