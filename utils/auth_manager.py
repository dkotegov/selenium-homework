import os


class AuthManager:
    ENV_AUTH_LOGIN = 'LOGIN'
    ENV_AUTH_PASSWORD = 'PASSWORD'

    @classmethod
    def get_login(cls, ending=''):
        # return os.environ.get(cls.ENV_AUTH_LOGIN + ending)
        return 'technopark50'

    @classmethod
    def get_password(cls, ending=''):
        # return os.environ.get(cls.ENV_AUTH_PASSWORD + ending)
        return 'testQA1'
