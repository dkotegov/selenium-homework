# coding=utf-8
from seismograph.ext import selenium
from pages.auth_page import AuthPage
from pages.feed_page import FeedPage

suite = selenium.Suite(__name__)


@suite.register
def test_auth(case, browser):
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.auth('89260665086',
                   'Gfhjkmlkzjr1488')

    feed_page = FeedPage(browser)
    feed_page.open()
    feed_page.popular_posts()



