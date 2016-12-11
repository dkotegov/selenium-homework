# coding=utf-8
from seismograph.ext import selenium
from pages.auth_page import AuthPage
from pages.feed_page import FeedPage
from pages.video_page import VideoPage
from pages.photo_page import PhotoPage
from pages.someone_post_page import ElsePostPage
import time
suite = selenium.Suite(__name__)

# @suite.register
# def test_make_repost_Video(case, browser):
#     auth_page = AuthPage(browser)
#     auth_page.open()
#     auth_page.auth('89260665086',
#                    'Gfhjkmlkzjr1488')
#
#     video_page = VideoPage(browser)
#     video_page.open()
#     time.sleep(1)
#     val = video_page.repostVideo()
#     if val == u'Опубликовано!':
#         return True
#     else:
#         return False

# @suite.register
# def test_make_repost_Photo(case, browser):
#     auth_page = AuthPage(browser)
#     auth_page.open()
#     auth_page.auth('89260665086',
#                    'Gfhjkmlkzjr1488')
#
#     photo_page = PhotoPage(browser)
#     photo_page.open()
#     time.sleep(1)
#     val = photo_page.repostPhoto()
#     if val == u'Опубликовано!':
#         return True
#     else:
#         return False

# @suite.register
# def test_make_repost_else_post(case, browser):
#     auth_page = AuthPage(browser)
#     auth_page.open()
#     auth_page.auth('89260665086',
#                    'Gfhjkmlkzjr1488')
#
#     else_post_page = ElsePostPage(browser)
#     else_post_page.open()
#     time.sleep(1)
#     val = else_post_page.makeRepost()
#     if val == u'Опубликовано!':
#         return True
#     else:
#         return False

# @suite.register
# def test_make_repost_else_post(case, browser):
#     auth_page = AuthPage(browser)
#     auth_page.open()
#     auth_page.auth('89260665086',
#                    'Gfhjkmlkzjr1488')
#
#     else_post_page = ElsePostPage(browser)
#     else_post_page.open()
#     time.sleep(1)
#     val = else_post_page.makeRepost()
#     if val == u'Опубликовано!':
#         browser.refresh()
#         time.sleep(3)
#         val = else_post_page.makeRepost()
#         if val == u'Опубликовано!':
#             return True
#         else:
#             return False
#     else:
#         return False

