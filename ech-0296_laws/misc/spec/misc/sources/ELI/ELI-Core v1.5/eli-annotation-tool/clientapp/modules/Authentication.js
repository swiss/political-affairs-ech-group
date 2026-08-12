// -*- coding: utf-8 -*-
// Project sponsor is https://ec.europa.eu/isa2/
// License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

/* global FormData */

import React from 'react';
import { Link } from 'react-router';

import JSForm from 'react-jsonschema-form';
import { api_fetch } from './API';

/*
const get_authuser = () => {
    const cookies = {};
    decodeURIComponent(document.cookie)
        .split(';')
        .map(item => { const [k,v] = item.split('='); cookies[k] = v; });
    console.log('cookies',cookies,document.cookie);
    return {login: cookies.user_name, admin: (cookies.user_admin === 'true')};
};
 */

class Login extends React.Component {

    constructor(props, context) {
        super(props, context);
        this.state = {error: null};
        this.submit = this.submit.bind(this);
    }

    submit({formData}) {
        const body = new FormData;
        for (let prop of Object.keys(formData)) {
            body.append(prop, formData[prop]);
        }
        api_fetch('/login', 'POST', {body: body})
            .then(response => {
                if (response.ok) {
                    response.json()
                        .then(js => {
                            this.props.changeUser(js.data);
                            this.context.router.push('/');
                        });
                } else {
                    console.warn("Response not ok",response.status);
                    throw new Error();
                }
            }).catch(e => this.setState({error: this.props.localize("loginError")}));
    }

    render() {
        return <LoginView localize={this.props.localize}
                          onSubmit={this.submit}
                          errorMsg={this.state.error} />;
    }

}
Login.contextTypes = {
    router: React.PropTypes.object
};

const LoginView = (props) => {

    const schema = {
        'title': props.localize("logIn"),
        'type': 'object',
        'required': ['username', 'password'],
        'properties': {
            'username': {
                'type': 'string',
                'title': props.localize("userName")
            },
            'password': {
                'type': 'string',
                'title': props.localize("password")
            }
        }
    };

    const uiSchema = {
        'username': {
            'ui:autofocus': true
        },
        'password': {
            'ui:widget': 'password'
        }
    };

    let error = null;
    if (props.errorMsg) {
        error = (
            <div className="alert alert-danger">
                {props.errorMsg}
            </div>
        );
    }

    return (
        <div className='container'>
            {error}
            <JSForm schema={schema} uiSchema={uiSchema} onSubmit={props.onSubmit} >
            <div>
            <button type="button" className="btn btn-primary" type="submit">{props.localize("submit")}</button>
            </div>
            </JSForm>
        </div>
    );
};
LoginView.propTypes = {
    localize: React.PropTypes.func.isRequired,
    onSubmit: React.PropTypes.func.isRequired,
    errorMsg: React.PropTypes.string
};

class Logout extends React.Component {
    constructor(props) {
        super(props);
        this.state = {logged: true};
        this.componentDidMount = this.componentDidMount.bind(this);
    }
    componentDidMount() {
        api_fetch('/logout', 'POST')
            .then(response => {
                if (response.ok) {
                    response.json()
                        .then(js => {
                            this.setState({logged: false});
                            this.props.changeUser(js.data);
                        });
                }
            });
    }
    render() {
        return (this.state.logged
                ? (<div className="container">{this.props.localize("loggingOut")}</div>)
                : (<div className="container">{this.props.localize("loggedOut")} <Link to="/login"><span className="glyphicon glyphicon-log-in"></span></Link></div>));
    }
}

export { Login, LoginView, Logout };
