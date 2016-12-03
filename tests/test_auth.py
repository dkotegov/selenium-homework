import os

from seismograph.ext import selenium
from seismograph.utils.common import waiting_for

from utils.auth_manager import AuthManager
from utils.pages import AuthPage

suite = selenium.Suite(__name__)


@suite.register
def test_auth(case, browser):
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.auth(AuthManager.get_login(),
                   AuthManager.get_password())


