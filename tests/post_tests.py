# coding=utf-8
from seismograph.ext import selenium
from pages.auth_page import AuthPage
from pages.group_page import PostPage
from pages.profile_page import ProfilePage
from pages.feed_page import FeedPage
from smth.auth import AuthManager

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

    feed_page = FeedPage(browser)
    feed_page.show_post()

    post_page = PostPage(browser)
    post_page.wait_overlay()
    post_page.create_post(text)

    profile_page = ProfilePage(browser)
    profile_page.open()
    profile_page.check_first_post(text)


@suite.register
def test_delete_own_post(case, browser):
    text = 'Test number 2'
    auth(case, browser)

    feed_page = FeedPage(browser)
    feed_page.show_post()

    post_page = PostPage(browser)
    post_page.wait_overlay()
    post_page.create_post(text)

    profile_page = ProfilePage(browser)
    profile_page.open()
    profile_page.check_first_post(text)
    profile_page.delete_my_post()
