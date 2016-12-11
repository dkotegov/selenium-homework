# coding=utf-8
from seismograph.ext import selenium
from pages.auth_page import AuthPage
from pages.feed_page import FeedPage
import time

from pages.group_post_page import PostPage as GPP

suite = selenium.Suite(__name__)


# @suite.register
# def test_get_author_group(case, browser):
#     auth_page = AuthPage(browser)
#     auth_page.open()
#     auth_page.auth('89260665086',
#                    'Gfhjkmlkzjr1488')
#
#     feed_page = FeedPage(browser)
#     content = feed_page.getPopularContent()
#     element, url = feed_page.getAuthor(content)
#     element.click()
#     time.sleep(3)
#     if url in browser.current_url:
#         return True
#     else:
#         return False
#
# @suite.register
# def test_get_post(case, browser):
#     auth_page = AuthPage(browser)
#     auth_page.open()
#     auth_page.auth('89260665086',
#                    'Gfhjkmlkzjr1488')
#
#     feed_page = FeedPage(browser)
#     time.sleep(1)
#     content = feed_page.getPopularContent()
#     content.click()
#     time.sleep(3)
#     url = browser.current_url
#     if "/topic/" in url:
#         return True
#     else:
#         return False
#
# @suite.register
# def test_get_post(case, browser):
#     auth_page = AuthPage(browser)
#     auth_page.open()
#     auth_page.auth('89260665086',
#                    'Gfhjkmlkzjr1488')
#
#     feed_page = FeedPage(browser)
#     time.sleep(1)
#     before = feed_page.getStatusLikes()
#     feed_page.makeLikeOnOwnPost()
#     after = feed_page.getStatusLikes()
#     if before != after:
#         return True
#     else:
#         return False
#
# @suite.register
# def test_make_repost(case, browser):
#     auth_page = AuthPage(browser)
#     auth_page.open()
#     auth_page.auth('89260665086',
#                    'Gfhjkmlkzjr1488')
#
#     feed_page = FeedPage(browser)
#     time.sleep(1)
#     content = feed_page.getPopularContent()
#     feed_page.makeRepost()
#     a = 5
#     b = 7

# @suite.register
# def test_make_self_comment(case, browser):
#     auth_page = AuthPage(browser)
#     auth_page.open()
#     auth_page.auth('89260665086',
#                    'Gfhjkmlkzjr1488')
#
#     feed_page = FeedPage(browser)
#     time.sleep(1)
#     content = feed_page.getPopularContent()
#     feed_page.makeSelfComment(content, feed_page)
#
#
# @suite.register
# def test_make_comment(case, browser):
#     auth_page = AuthPage(browser)
#     auth_page.open()
#     auth_page.auth('89260665086',
#                    'Gfhjkmlkzjr1488')
#
#     feed_page = FeedPage(browser)
#     time.sleep(1)
#     content = feed_page.getPopularContent()
#     feed_page.makeComment(content, feed_page)


# @suite.register
# def test_make_like(case, browser):
#     auth_page = AuthPage(browser)
#     auth_page.open()
#     auth_page.auth('89260665086',
#                    'Gfhjkmlkzjr1488')
#
#     feed_page = FeedPage(browser)
#     time.sleep(1)
#     content = feed_page.getPopularContent()
#     feed_page.makeLikeOnSelfComment(content, feed_page)
#
#
# @suite.register
# def test_make_double_like(case, browser):
#     auth_page = AuthPage(browser)
#     auth_page.open()
#     auth_page.auth('89260665086',
#                    'Gfhjkmlkzjr1488')
#
#     feed_page = FeedPage(browser)
#     time.sleep(1)
#     content = feed_page.getPopularContent()
#     feed_page.makeDoubleLike(content, feed_page)
#
#
#
# @suite.register
# def test_make_someone_like_comment(case, browser):
#     auth_page = AuthPage(browser)
#     auth_page.open()
#     auth_page.auth('89260665086',
#                    'Gfhjkmlkzjr1488')
#
#     feed_page = FeedPage(browser)
#     time.sleep(1)
#     content = feed_page.getPopularContent()
#     feed_page.makeLikeForSomemoneComment(content, feed_page)
#


@suite.register
def test_make_group_comment(case, browser):
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.auth('89260665086',
                   'Gfhjkmlkzjr1488')

    post_page = GPP(browser)
    post_page.open()
    time.sleep(1)
    post_page.makeGroupComment()

=======
    val =  feed_page.makeRepost()
    if val == u'Опубликовано!':
        return True
    else:
        return False




