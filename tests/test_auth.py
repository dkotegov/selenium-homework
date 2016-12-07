# coding=utf-8
import time
from seismograph.ext import selenium

from utils.auth_manager import AuthManager
from utils.auth_pages import AuthPage

suite = selenium.Suite(__name__)


@suite.register
def test_auth(case, browser):
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.auth(AuthManager.get_login(),
                   AuthManager.get_password())

