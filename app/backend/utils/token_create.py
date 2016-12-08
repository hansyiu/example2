# -*- coding: utf-8 -*-
import json
from app import settings
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

SECRET_KEY = settings.SECRET_KEY


class TToken(object):
    def __init__(self, name):
        self.name = name

    def generate_auth_token(self, expiration=1800):
        s = Serializer(SECRET_KEY, expires_in=expiration)
        return s.dumps({'name': self.name})

    def verify_auth_token(self, token):
        s = Serializer(SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            # valid token, but expired
            return json.dumps({'error': 'token expired'})
        except BadSignature:
            # invalid token
            return json.dumps({'error': 'invalid token'})
        # return data['name'] == self.name
        return data


# s1 = TToken('admin')
# to = s1.generate_auth_token()
# print(str(to, encoding='utf-8'))


