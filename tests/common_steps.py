import seismograph
from seismograph.ext import selenium

from pages.auth_page import AuthPage
from utils.auth_manager import AuthManager


class AuthStep(selenium.Case):
    @seismograph.step(1, 'Login to ok.ru')
    def auth(self, browser):
        auth_page = AuthPage(browser)
        auth_page.open()
        auth_page.auth(AuthManager.get_login(),
                       AuthManager.get_password())
