// -*- coding: utf-8 -*-
// Project sponsor is https://ec.europa.eu/isa2/
// License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

import React from 'react';
import { Link } from 'react-router';

import { api_fetch } from './API';
import { Login } from './Authentication';

const NavLink = (props) => React.createElement(Link,
                                               Object.assign({}, props, {activeClassName: "active"}));


class About extends React.Component {
    constructor(props) {
	super(props);
	this.state = {
            about_text: null
        };
	this.loadDataFromServer = this.loadDataFromServer.bind(this);
    }
    loadDataFromServer() {
        const request = new XMLHttpRequest();
        request.onreadystatechange = evt => {
            if (request.readyState === 4 && request.status === 200) {
                this.setState({
                    about_text: request.responseXML.body.innerHTML
                });
            }
        };
        request.open("GET", "/resource/about/"+this.props.lang);
        request.responseType = "document";
        request.send();
    }
    componentDidMount() {
	this.loadDataFromServer();
    }
    render() {
        const loc = this.props.localize;
        return (<div className="container">
                <h1>{loc("aboutEliAnnotationTool")}</h1>
                <p><b>{loc("version")}</b> {this.props.toolVersion}</p>
                <div dangerouslySetInnerHTML={
                    {__html: this.state.about_text}
                }></div>
                </div>);
    }
}


class App extends React.Component {
    constructor(props, context) {
        super(props, context);
        this.state = {
            lang: "en",
            toolVersion: null,
            localization: null,
            user_name: null,
            user_admin: false
        };
        this.componentDidMount = this.componentDidMount.bind(this);
        this.changeUser = this.changeUser.bind(this);
        this.loadLocalization = this.loadLocalization.bind(this);
        this.localize = this.localize.bind(this);
    }
    componentDidMount() {
        api_fetch('/whoami', 'GET')
            .then(response => response.json())
            .then(js => {
                this.setState(js.data);
                this.loadLocalization();
            });
    }
    loadLocalization() {
        api_fetch('/localizations/'+this.state.lang, 'GET')
            .then(response => response.json())
            .then(l10n => this.setState({localization: l10n}));
    }
    changeUser(user) {
        this.setState(user);
    }
    localize(key, domain="uiMessages", component="label") {
        if (this.state.localization == null) {
            return (("key" === "loading")
                    ? "Loading..." : key);
        }
        const dom = this.state.localization[domain];
        if (domain === "uiMessages") {
            const val = ((dom !== undefined) ? dom[key] : undefined);
            return ((val !== undefined) ? val : key);
        } else {
            const valObj = ((dom !== undefined) ? dom[key] : undefined);
            const val = ((valObj !== undefined) ? valObj[component] : undefined);
            return ((val !== undefined) ? val : ((component === "label") ? key : undefined));
        }
    }
    render () {
        const loc = this.localize;;
        const is_auth = (this.state.user_name !== 'Anonymous') && (this.state.user_name !== null);
        const loginout = ((this.props.children.type.name === 'Login')
                          || (this.props.children.type.name === 'Logout'));
        const needlogin = (!loginout && !is_auth);
        const navlinks = [];
        /*let userlink = null; */
        if(!loginout && is_auth) {
            navlinks.push(['/notice',loc("notices")],
                          ['/vocabs',loc("vocabularies")]);
            if (this.state.user_admin)
                navlinks.push(['/formconfig',loc("forms")]);
            navlinks.push(['/about',loc("about")],
                          ['/logout',loc("logOut")+' ('+this.state.user_name+')']);
            /*userlink = (<li className="dropdown">
                        <a className="dropdown-toggle" data-toggle="dropdown" href="#">
                        <span className="glyphicon glyphicon-user"></span>Â 
                        {this.state.user_name}<span className="caret"></span></a>
                        <ul class="dropdown-menu">
                        <li><Link to="/logout">Log out</Link></li>
                        </ul>
                        </li>);*/
        }
        const navlist = navlinks.map(item =>
                                     <li key={item[0]}>
                                     <NavLink to={item[0]}>{item[1]}</NavLink>
                                     </li>);
        const please_login = (<div className='container'>{loc("welcomeLogIn")} <Link to="/login"><span className="glyphicon glyphicon-log-in"></span></Link></div>);
        const loading = <div className="container">
            {loc("welcomeLoading")}
          </div>;
        const childrenWithUserCB = (children) =>
                  React.Children.map(children,
                                     (child) =>
                                     React.cloneElement(child, {changeUser: this.changeUser,
                                                                localize: this.localize,
                                                                lang: this.state.lang,
                                                                toolVersion: this.state.toolVersion,
                                                                user: {name: this.state.user_name,
                                                                       admin: this.state.user_admin}
                                                               }));
        return (<div>
                <nav className="navbar navbar-default">
                <div className="container-fluid">
                <div className="navbar-header">
                <span className="navbar-brand">{loc("eliAnnotationTool")}</span>
                </div>
                <div className="navbar-collapse">
                <ul className="nav navbar-nav">
                {navlist}
                </ul>
                </div>
                </div>
                </nav>
                {(this.state.user_name === null)
                 ? loading
                 : (needlogin
                    ? please_login
                    : childrenWithUserCB(this.props.children))}
                </div>
               );
    }
};

export { App, About, NavLink };
