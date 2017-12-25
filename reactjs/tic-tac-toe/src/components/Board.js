/**
 * 棋盘面板
 */
import React from 'react';
import Square from './Square';
import calculateWinner from './calculate';

class Board extends React.Component {
    // 棋盘面板，3行3列，共9个正方形

    //  squares通过this.props.squares来获取了

    // constructor(props) {
    //     super(props);
    //     this.state = {
    //         squares: Array(9).fill(null),
    //         // 下一步是X还是O
    //         xIsNext: true,
    //         winner: null
    //     };
    // }

    handleClick(i) {
        //  把onClick的处理事件放到Game组件中了
        
        console.log(i);
        // 用slice去实现squares数组的copy
        const squares = this.state.squares.slice();

        // 如果已经有winner或者当前格子已经有值，就不做任何操作
        if (this.state.winner || squares[i]) {
            return;
        }
        
        squares[i] = this.state.xIsNext ? 'X' : 'O';
        var winner = calculateWinner(squares);
        this.setState({
                squares: squares,
                xIsNext: !this.state.xIsNext,
                winner: winner,
            });
    }

    renderSquare(i) {
        return (
            <Square
              value={this.props.squares[i]}
              onClick={() => this.props.onClick(i)}
            />
        );
    }

    render() {
        // 把squares传入计算赢家的算法中
        // const winner = calculateWinner(this.state.squares);
        // let status;
        // if (winner) {
        //     status = 'Winner: ' + winner;
        // }else {
        //     status = 'Next player: ' + (this.state.xIsNext ? 'X' : 'O');
        // }

        return (
            <div>
                {/* <div className="status">{status}</div> */}
                <div className="board-row">
                    {this.renderSquare(0)}
                    {this.renderSquare(1)}
                    {this.renderSquare(2)}
                </div>
                
                <div className="board-row">
                    {this.renderSquare(3)}
                    {this.renderSquare(4)}
                    {this.renderSquare(5)}
                </div>

                <div className="board-row">
                    {this.renderSquare(6)}
                    {this.renderSquare(7)}
                    {this.renderSquare(8)}
                </div>
            </div>
        );
    }
}

export default Board;