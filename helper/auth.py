import os


class AuthManager:
    def __init__(self):
        pass

    AUTH_LOGIN = 'LOGIN'
    AUTH_PASSWORD = 'PASSWORD'

    @staticmethod
    def get_login():
        return os.environ.get(AuthManager.AUTH_LOGIN)

    @staticmethod
    def get_password():
        return os.environ.get(AuthManager.AUTH_PASSWORD)
