# coding=utf-8
from seismograph.ext import selenium
from pages.auth_page import AuthPage
from pages.feed_page import FeedPage
from pages.profile_page import ProfilePage
from smth.Auth import AuthManager

from pages.group_post_page import GroupPage

suite = selenium.Suite(__name__)


def auth(case, browser):
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.auth(AuthManager.get_login(),
                   AuthManager.get_password())


# @suite.register
def test_get_author_group(case, browser):
    auth(case, browser)
    feed_page = FeedPage(browser)
    content = feed_page.get_popular_content()
    element, url = feed_page.getAuthor(content)
    element.click()
    assert url in browser.current_url


# @suite.register
def test_get_post(case, browser):
    auth(case, browser)

    feed_page = FeedPage(browser)
    content = feed_page.get_popular_content()
    content.click()
    url = browser.current_url
    return "/topic/" in url


# @suite.register
def test_get_post(case, browser):
    auth(case, browser)

    feed_page = FeedPage(browser)
    before = feed_page.get_status_likes()
    feed_page.make_like_on_own_post()
    after = feed_page.get_status_likes()
    return before != after


# @suite.register
def test_make_self_comment(case, browser):
    auth(case, browser)

    feed_page = FeedPage(browser)
    content = feed_page.get_popular_content()
    feed_page.make_self_comment(content, feed_page)


# @suite.register
def test_make_comment(case, browser):
    auth(case, browser)

    feed_page = FeedPage(browser)
    content = feed_page.get_popular_content()
    feed_page.make_comment(content, feed_page)


# @suite.register
def test_make_like(case, browser):
    auth(case, browser)

    feed_page = FeedPage(browser)
    feed_page.make_like_on_self_comment(feed_page)


# @suite.register
def test_make_double_like(case, browser):
    auth(case, browser)

    feed_page = FeedPage(browser)
    feed_page.make_double_like(feed_page)


# @suite.register
def test_make_someone_like_comment(case, browser):
    auth(case, browser)

    feed_page = FeedPage(browser)
    feed_page.make_like_for_someone_comment(feed_page)


# @suite.register
def test_make_group_comment(case, browser):
    auth(case, browser)

    group_page = GroupPage(browser)
    group_page.open()
    group_page.open_post_comments()
    group_page.make_group_comment()


# @suite.register
def test_make_repost(case, browser):
    auth(case, browser)

    feed_page = FeedPage(browser)
    val = feed_page.make_repost()
    assert u'Опубликовано!' in val


# @suite.register
def test_make_two_likes(case, browser):
    auth(case, browser)

    feed_page = FeedPage(browser)
    feed_page.make_like_two_likes()


# @suite.register
def test_make_one_like(case, browser):
    auth(case, browser)

    feed_page = FeedPage(browser)
    feed_page.make_one_like()


# @suite.register
def test_make_repost_by_double_click(case, browser):
    auth(case, browser)

    feed_page = FeedPage(browser)
    val = feed_page.make_double_click_repost()
    assert u'Опубликовано!' in val


@suite.register
def test_make_repost_and_delete(case, browser):
    auth(case, browser)

    feed_page = FeedPage(browser)
    val = feed_page.make_repost()
    assert u'Опубликовано!' in val

    profile_page = ProfilePage(browser)
    profile_page.open()
    profile_page.delete_my_post()
