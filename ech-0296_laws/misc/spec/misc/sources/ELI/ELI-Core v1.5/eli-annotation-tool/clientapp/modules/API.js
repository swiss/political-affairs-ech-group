// -*- coding: utf-8 -*-
// Project sponsor is https://ec.europa.eu/isa2/
// License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

/* global fetch */

require('babel-polyfill');
require('isomorphic-fetch');

import React from 'react';
import Form from 'react-jsonschema-form';

const mk_error = (name) => {
    function CustomError(message) {
        this.name = name;
        this.message = message || name;
        this.stack = (new Error()).stack;
    };
    CustomError.prototype = Object.create(Error.prototype);
    CustomError.prototype.constructor = CustomError;
    return CustomError;
};

const UnauthorizedError = mk_error('UnauthorizedError');

const api_fetch = (endpoint, method, opts={}) => {
    const options = Object.assign({
        method: method,
        credentials: 'include',
        headers: {
            Accept: 'application/json',
        },
    }, opts);
    return fetch(endpoint, options);
/*        .then(response => {
            if (response.status === 401) throw new UnauthorizedError(endpoint);
            else return new Promise(resolve => resolve(response));
        });*/
};

export { api_fetch };
