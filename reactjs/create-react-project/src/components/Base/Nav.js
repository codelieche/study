/**
 * 这个是站点左侧导航
 * 菜单有2级，
 *    1. 如果subs就表示是有两层的
 *    2. 有url就表示一级菜单直接跳去页面
 * 注意事项：
 *    1. 如果navData既有url又有subs，暂时会以subs为主
 *    2. 后续可调整
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
            // 情况一：当侧边栏收起的时候
            navLeftClass = "menu-left menu-small";

            // 根据navData渲染导航菜单元素
            topMenuElements = this.state.navData.map((item, index) => {
                // 第1步：处理一级菜单
                // 1-1: 先处理一级菜单元素class
                var topMenuClass = "top-menu";
                if (this.state.openTopMenuKey === item.key) {
                    topMenuClass = "top-menu active";
                }
                var hasSubsMenu = false;
                if (item.subs && item.subs instanceof Array) {
                    hasSubsMenu = true;
                    topMenuClass += " subs";
                } else {
                    topMenuClass += " no-subs";
                }

                // 第2步：成二级菜单元素
                var subMenuItems;
                if (hasSubsMenu) {
                    subMenuItems = item.subs.map((v, i) => {
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

                }

                // 第3步：返回一级菜单元素
                // 如果hasSubsMenu为真:就（内嵌二级菜单元素列表）
                if (hasSubsMenu) {
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
                } else {
                    // 只需要返回一级菜单即可
                    return (
                        <div className={topMenuClass} key={index}>
                            <Tooltip title={item.title} placement='right' overlayStyle={{ opacity: 1 }}>
                                <NavLink to={item.url} activeClassName="active">
                                    <div className="top-menu-title" onClick={() => { this.topMenuOnClick(item.key) }}>
                                        <Icon type={item.icon} />
                                    </div>
                                </NavLink>
                            </Tooltip>
                            {/*二级菜单列表  */}
                        </div>
                    );
                }
            });
        } else {
            // 情况二：当侧边栏展开的时候，不用Tooltip，而使用title了
            // 第1步：处理一级菜单
            navLeftClass = "menu-left";
            topMenuElements = this.state.navData.map((item, index) => {
                // 在生成top-menu元素
                // 1-1：先定义顶级菜单的样式
                var topMenuClass = "top-menu";
                if (this.state.openTopMenuKey === item.key) {
                    // 当展开的key 与当前菜单的key相同的时候，加上active的class
                    topMenuClass = "top-menu active";
                }
                // 一级菜单可能有子菜单：也可能没有
                var hasSubsMenu = false;
                if (item.subs && item.subs instanceof Array) {
                    // 如果当前元素有subs，就是有二级菜单的
                    topMenuClass += " subs";
                    hasSubsMenu = true;
                } else {
                    topMenuClass += " no-subs";
                }

                // 第2步：生成二级菜单menu元素
                var subMenuItems;
                if (hasSubsMenu) {
                    // 渲染二级菜单元素
                    subMenuItems = item.subs.map((v, i) => {
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
                }

                // 第3步：返回一级菜单元素
                // 如果hasSubsMenu为真:就（内嵌二级菜单元素列表）
                if (hasSubsMenu) {
                    // 有二级元素
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
                } else {
                    // 无二级元素
                    return (
                        <div className={topMenuClass} key={index} sroll="no">
                            <NavLink to={item.url} activeClassName="active">
                                <div className="top-menu-title">
                                    <Icon type={item.icon} />
                                    <span className="title">{item.title}</span>
                                </div>
                            </NavLink>
                            {/*无二级菜单元素  */}
                        </div>
                    );
                }

            });
        }
        return (
            <div className={navLeftClass}>
                {topMenuElements}
            </div>
        );

    }
}