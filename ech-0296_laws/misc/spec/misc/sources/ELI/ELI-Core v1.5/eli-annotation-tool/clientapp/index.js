// -*- coding: utf-8 -*-
// Project sponsor is https://ec.europa.eu/isa2/
// License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

import React from 'react';
import { render } from 'react-dom';
import { Router, Route, browserHistory, IndexRoute } from 'react-router';
import { App, About } from './modules/App';
import { Vocabs } from './modules/Vocabs';
import {Notice, NoticeRdfImport} from './modules/Notice';
import { ManageForms, Form } from './modules/Form';
import { Login, Logout } from './modules/Authentication';

render((<Router history={browserHistory}>
          <Route path="/" component={App}>
            <IndexRoute component={Notice}/>
            <Route path="/notice" component={Notice}/>
            <Route path="/notice/import" component={NoticeRdfImport}/>
            <Route path="/vocabs" component={Vocabs}/>
            <Route path="/form/:formName" component={Form}/>
            <Route path="/form/:formName/:noticeURI" component={Form}/>
            <Route path="/formconfig" component={ManageForms} />
            <Route path="/formconfig/:formName" component={Form}/>
            <Route path="/about" component={About}/>
            <Route path="/login" component={Login}/>
            <Route path="/logout" component={Logout}/>
          </Route>
        </Router>),
       document.getElementById('app'));
