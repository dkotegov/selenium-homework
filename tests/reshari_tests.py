# coding=utf-8
from seismograph.ext import selenium
from pages.auth_page import AuthPage
from smth.Auth import AuthManager
from pages.video_page import VideoPage
from pages.photo_page import PhotoPage
from pages.someone_post_page import ElsePostPage

suite = selenium.Suite(__name__)


def auth(case, browser):
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.auth(AuthManager.get_login(),
                   AuthManager.get_password())


@suite.register
def test_make_repost_video(case, browser):
    auth(case, browser)
    video_page = VideoPage(browser)
    video_page.open()
    val = video_page.repost_video()
    assert u'Опубликовано!' in val


@suite.register
def test_make_repost_photo(case, browser):
    auth(case, browser)
    photo_page = PhotoPage(browser)
    photo_page.open()
    val = photo_page.repost_photo()
    assert u'Опубликовано!' in val


@suite.register
def test_make_repost_else_post(case, browser):
    auth(case, browser)
    else_post_page = ElsePostPage(browser)
    else_post_page.open()
    val = else_post_page.make_repost()
    assert u'Опубликовано!' in val


@suite.register
def test_make_double_repost_else_post(case, browser):
    auth(case, browser)
    else_post_page = ElsePostPage(browser)
    else_post_page.open()
    val = else_post_page.make_repost()
    assert u'Опубликовано!' in val

    else_post_page.open()
    val = else_post_page.make_repost()
    assert u'Опубликовано!' in val
