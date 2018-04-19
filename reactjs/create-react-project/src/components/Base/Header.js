import React from 'react';
import { Link } from 'react-router-dom';

import logo from '../../asset/images/logo.svg';

export default class Header extends React.Component {
    render() {
        return (
            <div>
                <Link to="/" className="logo">
                    <img src={logo} alt="首页" />
                </Link>
                <ul className="nav">
                    <li>
                        <a target="blank">热门</a>
                    </li>
                    <li>
                        <a target="blank">推荐</a>
                    </li>
                    <li>
                        <a target="blank">专题</a>
                    </li>
                    <li>
                        <a target="blank">个人中心</a>
                    </li>
                </ul>
            </div>
        );
    }
}