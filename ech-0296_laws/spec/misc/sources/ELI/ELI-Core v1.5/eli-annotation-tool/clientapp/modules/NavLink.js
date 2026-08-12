// -*- coding: utf-8 -*-
// Project sponsor is https://ec.europa.eu/isa2/
// License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

import React from 'react';
import { Link } from 'react-router';

const NavLink = (props) => (<Link {...props} activeClassName="active"/>);

export default NavLink;
