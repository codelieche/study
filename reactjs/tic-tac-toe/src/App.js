/**
 * 棋盘游戏主程序
 */
import React from 'react';
import Board from './components/Board';
import calculateWinner from './components/calculate';

class Game extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            history: [{
                squares: Array(9).fill(null),
            }],
            stepNumber: 0,
            xIsNext: true,
        }
    }

    handeleClick(i) {
        console.log(i);
        // 在jumperTo中就修改了history了，所以这里可以直接使用history
        // 或者根据stepNumber来确定history
        // const history = this.state.history.slice(0, this.state.stepNumber + 1);

        const history = this.state.history;
        const current = history[history.length - 1];
        const squares = current.squares.slice();

        if (calculateWinner(squares) || squares[i]) {
            return;
        }

        squares[i] = this.state.xIsNext ? 'X' : 'O';
        this.setState({
            history: history.concat([{
                squares: squares,
            }]),
            xIsNext: !this.state.xIsNext,
        });
    }

    jumpTo(step) {
        // 跳到第几步
        this.setState(prevState => {
            // 先取出老的history
            var history = prevState.history;
            var newHistory = history.slice(0, step + 1);
            return {
                history: newHistory,
                // 修改step和xIsNext
                stepNumber: step,
                xIsNext: (step % 2) === 0,
            };
        });
    }

    render() {
        // 获取history
        const history = this.state.history;
        const current = history[history.length - 1];
        const winner = calculateWinner(current.squares);

        // 历史记录
        const moves = history.map((step, move) => {
            const desc = move ?
              'Go to move #' + move :
              'Go to game start';
            
            return (
                <li key={move}>
                    <button onClick={() => this.jumpTo(move)}>{desc}</button>
                </li>
            );
        });

        let status;
        if (winner) {
            status = 'Winner: ' + winner;
        }else {
            status = 'Next player: ' + (this.state.xIsNext ? 'X' : 'O');
        }

        return (
            <div className="game">
                <div className="game-board">
                    <Board
                      squares={current.squares}
                      onClick={(i) => this.handeleClick(i)}
                    />
                </div>
                <div className="game-info">
                    <div>{status}</div>
                    <ol>{moves}</ol>
                </div>
            </div>
        );
    }
}

export default Game;