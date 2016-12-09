# coding=utf-8
from seismograph.ext import selenium
from pages.auth_page import AuthPage
from pages.feed_page import FeedPage
import time
suite = selenium.Suite(__name__)


@suite.register
def test_get_author_group(case, browser):
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.auth('89260665086',
                   'Gfhjkmlkzjr1488')

    feed_page = FeedPage(browser)
    content = feed_page.getPopularContent()
    element, url = feed_page.getAuthor(content)
    element.click()
    time.sleep(3)
    if url in browser.current_url:
        return True
    else:
        return False

@suite.register
def test_get_post(case, browser):
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.auth('89260665086',
                   'Gfhjkmlkzjr1488')

    feed_page = FeedPage(browser)
    time.sleep(1)
    content = feed_page.getPopularContent()
    content.click()
    time.sleep(3)
    url = browser.current_url
    if "/topic/" in url:
        return True
    else:
        return False

@suite.register
def test_get_post(case, browser):
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.auth('89260665086',
                   'Gfhjkmlkzjr1488')

    feed_page = FeedPage(browser)
    time.sleep(1)
    before = feed_page.getStatusLikes()
    feed_page.makeLikeOnOwnPost()
    after = feed_page.getStatusLikes()
    if before != after:
        return True
    else:
        return False





