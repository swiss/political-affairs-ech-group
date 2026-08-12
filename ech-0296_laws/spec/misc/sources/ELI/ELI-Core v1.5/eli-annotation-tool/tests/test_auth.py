# Project sponsor is https://ec.europa.eu/isa2/
# License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

import json
import os
import tempfile
import unittest

import flask

from eli_annotation.__main__ import app
from eli_annotation import auth


class AuthTC(unittest.TestCase):

    users = {
        'bob': {
            'password': auth.hash_password('secret'),
            'fullname': 'Robert Bobby',
            'admin': False,
            'enabled': True
        },
        'john': {
            'password': auth.hash_password('secret'),
            'fullname': 'John Johnny',
            'admin': False,
            'enabled': False
        },
        'helen': {
            'password': auth.hash_password('secret'),
            'fullname': 'Helen Lenny',
            'admin': True,
            'enabled': True
        },
    }

    headers = [('Accept', 'application/json')]

    def setUp(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            app.login_manager.users_database = f.name
            json.dump(self.users, f)
        app.config['SECRET_KEY'] = 'secret'
        self.users_dbfile = f.name
        self.app = app

    def tearDown(self):
        os.unlink(self.users_dbfile)

    def test_login_logout(self):
        with self.app.test_client() as c:
            self.assertFalse(c.cookie_jar)
            r = c.post('/login', headers=self.headers,
                       data={'username': 'bob', 'password': 'secret'})
            self.assertEqual(r.status_code, 200)
            self.assertTrue(c.cookie_jar)
            self.assertEqual(flask.session['user_id'], 'bob')
            r = c.post('/logout', headers=self.headers)
            self.assertEqual(r.status_code, 200)
            self.assertNotIn('username', flask.session)
            r = c.post('/logout', headers=self.headers)
            self.assertEqual(r.status_code, 200) # XXX 401 instead ?

    def test_login_failed(self):
        with self.app.test_client() as c:
            r = c.post('/login', headers=self.headers,
                       data={'username': 'bob', 'password': 'bad pass'})
            self.assertEqual(r.status_code, 401)
            r = c.post('/login', headers=self.headers,
                       data={'username': 'unknown', 'password': 'x'})
            self.assertEqual(r.status_code, 401)

    def test_login_disabled(self):
        with self.app.test_client() as c:
            r = c.post('/login', headers=self.headers,
                       data={'username': 'john', 'password': 'secret'})
            self.assertEqual(r.status_code, 401)



if __name__ == '__main__':
    unittest.main()
