# -*- coding: utf-8 -*-
import os


class AuthManager:
    def __init__(self):
        pass

    ENV_AUTH_LOGIN = 'LOGIN'
    ENV_AUTH_PASSWORD = 'PASSWORD'

    @classmethod
    def get_login(cls, ending=''):
        return os.environ.get(cls.ENV_AUTH_LOGIN)

    @classmethod
    def get_password(cls, ending=''):
        return os.environ.get(cls.ENV_AUTH_PASSWORD)
