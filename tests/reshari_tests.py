# coding=utf-8
from seismograph.ext import selenium
from pages.auth_page import AuthPage
from pages.feed_page import FeedPage
from pages.video_page import VideoPage
import time
suite = selenium.Suite(__name__)

@suite.register
def test_make_repost(case, browser):
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.auth('89260665086',
                   'Gfhjkmlkzjr1488')

    video_page = VideoPage(browser)
    video_page.open()
    time.sleep(1)
    val = video_page.repostVideo()
    if val == u'Опубликовано!':
        return True
    else:
        return False