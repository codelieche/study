/**
 * 棋盘面板
 */
import React from 'react';
import Square from './Square';

class Board extends React.Component {
    // 棋盘面板，3行3列，共9个正方形
    constructor(props) {
        super(props);
        this.state = {
            squares: Array(9).fill(null),
            // 下一步是X还是O
            xIsNext: true,
        };
    }

    handleClick(i) {
        console.log(i);
        // 用slice去实现squares数组的copy
        const squares = this.state.squares.slice();
        squares[i] = this.state.xIsNext ? 'X' : 'O';
        this.setState({
                squares: squares,
                xIsNext: !this.state.xIsNext
            });
    }

    renderSquare(i) {
        return (
            <Square
              value={this.state.squares[i]}
              onClick={() => this.handleClick(i)}
            />
        );
    }

    render() {
        const status = 'Next player: ' + (this.state.xIsNext ? 'X' : 'O');

        return (
            <div>
                <div className="status">{status}</div>
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