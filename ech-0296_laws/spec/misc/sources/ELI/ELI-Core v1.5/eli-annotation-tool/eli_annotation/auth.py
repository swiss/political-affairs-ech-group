# Project sponsor is https://ec.europa.eu/isa2/
# License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

import json

import bcrypt
from flask_login import UserMixin


def hash_password(pw):
    pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
    if isinstance(pwhash, str):
        return pwhash
    return pwhash.decode('utf8')


class ELIUser(UserMixin):

    @classmethod
    def get(cls, userdb_file, user_id):
        with open(userdb_file, encoding='utf-8') as userdb:
            users = json.load(userdb)
        userinfo = users.get(user_id)
        if userinfo is None:
            return None
        return cls(user_id,
                   admin=userinfo['admin'],
                   password=userinfo['password'],
                   enabled=userinfo['enabled'])

    def __init__(self, username, password, enabled, admin):
        self.username = username
        self.password = password
        self.admin = admin
        self.enabled = enabled

    def get_id(self):
        return self.username

    def __str__(self):
        return '<ELIUser {} ({}enabled) ({}authenticated)>'.format(
            self.username, "" if self.enabled else "not ",
            "" if self.is_authenticated else "not ")

    def check_password(self, password):
        expected_hash = self.password.encode('utf8')
        try:
            return bcrypt.checkpw(password.encode('utf8'), expected_hash)
        except ValueError:
            return False
