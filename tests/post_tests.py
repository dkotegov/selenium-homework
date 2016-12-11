# coding=utf-8
from seismograph.ext import selenium
from pages.auth_page import AuthPage
from pages.post_page import PostPage
from pages.profile_page import ProfilePage
from auth_tests import test_auth
import time

suite = selenium.Suite(__name__)


@suite.register
def test_post(case, browser):
    text = 'Test number 1'
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.auth('89260665086','Gfhjkmlkzjr1488')

    post_page = PostPage(browser)
    post_page.open()
    post_page.create_post(text)

    profile_page = ProfilePage(browser)
    profile_page.open()
    if profile_page.check_first_post(text):
        return True
    else:
        return False

@suite.register
def test_delete_own_post(case, browser):
    text = 'Test number 1'
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.auth('89260665086','Gfhjkmlkzjr1488')

    post_page = PostPage(browser)
    post_page.open()
    time.sleep(5)
    post_page.create_post(text)

    profile_page = ProfilePage(browser)
    profile_page.open()
    profile_page.check_first_post(text)
    if profile_page.delete_my_post():
        return True
    else:
        return False




