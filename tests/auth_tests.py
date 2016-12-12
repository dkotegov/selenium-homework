# coding=utf-8
from seismograph.ext import selenium
from pages.auth_page import AuthPage
from smth.Auth import AuthManager

suite = selenium.Suite(__name__)


@suite.register
def test_auth(case, browser):
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.auth(AuthManager.get_login(),
                   AuthManager.get_password())

