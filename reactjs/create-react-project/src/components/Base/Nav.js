/*
这个是站点左侧导航
*/
import React from 'react';
import {
    Icon,
    Tooltip,
} from 'antd';
import { NavLink } from 'react-router-dom';
// import '../../styles/less/nav.less';

import navData from './NavData';

export default class Nav extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            // navData: [],
            navData: navData,
            openTopMenuKey: this.props.defaultOpenKey,
            collapsed: this.props.collapsed,
        };
        this.topMenuOnClick = this.topMenuOnClick.bind(this);
    }

    componentDidMount() {
        // this.fetchNavData();
    }

    fetchNavData = () => {
        // 获取用户导航数据
    }

    topMenuOnClick(key) {
        // 设置当前展开的一级菜单key
        if (this.state.openTopMenuKey === key) {
            this.setState({
                openTopMenuKey: null,
            });
        } else {
            this.setState({
                openTopMenuKey: key,
            });
        }

    }

    static getDerivedStateFromProps(nextProps, prevState) {
        if (nextProps.defaultOpenKey !== prevState.openTopMenuKey) {
            return {
                openTopMenuKey: nextProps.defaultOpenKey
            };
        } else {
            return null;
        }
    }

    render() {
        // 先申明导航菜单元素，最外层的导航菜单class
        var topMenuElements, navLeftClass;
        if (this.props.collapsed) {
            // 当侧边栏收起的时候
            navLeftClass = "menu-left menu-small"
            // 根据navData渲染导航菜单元素
            topMenuElements = this.state.navData.map((item, index) => {
                // 先生成二级菜单元素
                var subMenuItems = item.subs.map((v, i) => {
                    return (
                        <Tooltip title={v.title} placement='right' key={i} >
                            <li className="sub-menu-item">
                                <NavLink to={v.slug} activeClassName="active">
                                    <Icon type={v.icon}></Icon>
                                </NavLink>
                            </li>
                        </Tooltip>
                    );
                });
                // 在生成一级菜单元素
                var topMenuClass = "top-menu";
                if (this.state.openTopMenuKey === item.key) {
                    topMenuClass = "top-menu active";
                }
                // 返回一级菜单元素（内嵌二级菜单元素列表）
                return (
                    <div className={topMenuClass} key={index}>
                        <Tooltip title={item.title} placement='right' overlayStyle={{ opacity: 1 }}>
                            <div className="top-menu-title" onClick={() => { this.topMenuOnClick(item.key) }}>
                                <Icon type={item.icon} />
                            </div>
                        </Tooltip>
                        {/*二级菜单列表  */}
                        <ul className="sub-menu-list">
                            {subMenuItems}
                        </ul>
                    </div>
                );
            });
        } else {
            // 当侧边栏展开的时候，不用Tooltip，而使用title了
            navLeftClass = "menu-left"
            topMenuElements = this.state.navData.map((item, index) => {
                // 先生成二级菜单menu元素
                var subMenuItems = item.subs.map((v, i) => {
                    return (
                        <li className="sub-menu-item" key={i}>
                            <NavLink to={v.slug} activeClassName="active">
                                <div className="sub-menu-title">
                                    <Icon type={v.icon}></Icon>
                                    <span className="title">{v.title}</span>
                                </div>
                            </NavLink>
                        </li>
                    );
                });
                // 在生成top-menu元素
                var topMenuClass = "top-menu";
                if (this.state.openTopMenuKey === item.key) {
                    // 当展开的key 与当前菜单的key相同的时候，加上active的class
                    topMenuClass = "top-menu active";
                }
                // 返回一级菜单元素（内嵌二级菜单元素列表）
                return (
                    <div className={topMenuClass} key={index} sroll="no">
                        <div className="top-menu-title" onClick={() => { this.topMenuOnClick(item.key) }}>
                            <Icon type={item.icon} />
                            <span className="title">{item.title}</span>
                        </div>
                        {/*二级菜单元素  */}
                        <ul className="sub-menu-list">
                            {subMenuItems}
                        </ul>
                    </div>
                );
            });
        }
        return (
            <div className={navLeftClass}>
                {topMenuElements}
            </div>
        );

    }
}