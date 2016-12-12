# coding=utf-8
from seismograph.ext import selenium
from pages.auth_page import AuthPage
from pages.post_page import PostPage
from pages.profile_page import ProfilePage
from smth.Auth import AuthManager
import time

suite = selenium.Suite(__name__)


def auth(case, browser):
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.auth(AuthManager.get_login(),
                   AuthManager.get_password())


@suite.register
def test_post(case, browser):
    text = 'Test number 1'
    auth(case, browser)

    post_page = PostPage(browser)
    post_page.open()
    post_page.create_post(text)

    profile_page = ProfilePage(browser)
    profile_page.open()
    return profile_page.check_first_post(text)


@suite.register
def test_delete_own_post(case, browser):
    text = 'Test number 2'
    auth(case, browser)

    post_page = PostPage(browser)
    post_page.open()
    time.sleep(5)
    post_page.create_post(text)

    profile_page = ProfilePage(browser)
    profile_page.open()
    profile_page.check_first_post(text)
    return profile_page.delete_my_post()
