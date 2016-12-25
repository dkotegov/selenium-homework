import os


class AuthManager:
    AUTH_LOGIN = '89260665086'
    AUTH_PASSWORD = 'Gfhjkmlkzjr1488'

    @staticmethod
    def get_login():
        return AuthManager.AUTH_LOGIN

    @staticmethod
    def get_password():
        return AuthManager.AUTH_PASSWORD
