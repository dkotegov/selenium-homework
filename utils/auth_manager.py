import os
from utils.credentials import LOGIN, PASSWORD

class AuthManager:
    ENV_AUTH_LOGIN = 'LOGIN'
    ENV_AUTH_PASSWORD = 'PASSWORD'

    @classmethod
    def get_login(cls, ending=''):
        # return os.environ.get(cls.ENV_AUTH_LOGIN + ending)
        return LOGIN

    @classmethod
    def get_password(cls, ending=''):
        # return os.environ.get(cls.ENV_AUTH_PASSWORD + ending)
        return PASSWORD
