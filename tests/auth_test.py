import seismograph
from seismograph.ext import selenium
from pages.auth_page import AuthPage
from smth.auth import AuthManager


class Auth(selenium.Case):

    @seismograph.step(1, 'Auth')
    def auth(self, browser):
        auth_page = AuthPage(browser)
        auth_page.open()
        auth_page.auth(AuthManager.get_login(),
                       AuthManager.get_password())
