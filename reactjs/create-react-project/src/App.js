import React, { Component } from 'react';
import {
  BrowserRouter as Router,
  Route,
  Switch,
} from 'react-router-dom';

import Home from './components/Home';
import Login from "./components/User/Login";
import Logout from "./components/User/Logout";
import Test from './components/Test';

// 按需加载，不需要引入antd.css
// import 'antd/dist/antd.css';
import './styles/main.less';

class App extends Component {
  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/user/login" component={Login} />
          <Route exact path="/user/logout" component={Logout} />
          <Route exact path="/" component={Home} />
          <Route path="/front" render={(props) => (<Home defaultOpenKey="front" {...props} />)} />
          <Route path="/backend" render={(props) => (<Home defaultOpenKey="backend" {...props} />)} />
          <Route path="/database" render={(props) => (<Home defaultOpenKey="database" {...props} />)} />
          <Route path="/cloud" render={(props) => (<Home defaultOpenKey="cloud" {...props} />)} />
          <Route path="/user" render={(props) => (<Home defaultOpenKey="user" {...props} />)} />
          <Route path="/test" component={Test} />
        </Switch>
      </Router>
    );
  }
}

export default App;