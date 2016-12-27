# coding=utf-8

import seismograph
from seismograph.ext import selenium
from auth_test import Auth
from pages.feed_page import FeedPage
from pages.profile_page import ProfilePage
from pages.video_page import VideoPage
from pages.photo_page import PhotoPage
from pages.someone_post_page import ElsePostPage


PUBLISHED = u'Опубликовано!'
HIDDEN = u'скрыто'

suite = selenium.Suite(__name__)


@suite.register
class TestRepostVideo(Auth):
    @seismograph.step(2, 'Test repost video')
    def repost_video(self, browser):
        video_page = VideoPage(browser)
        video_page.open()
        video_page.open_menu()
        val = video_page.repost_video()
        self.assertion.is_in(PUBLISHED, val)


@suite.register
class TestRepostPhoto(Auth):
    @seismograph.step(2, 'Test repost photo')
    def repost_photo(self, browser):
        photo_page = PhotoPage(browser)
        photo_page.open()
        photo_page.open_menu()
        val = photo_page.repost_photo()
        self.assertion.is_in(PUBLISHED, val)


def repost(browser):
    else_post_page = ElsePostPage(browser)
    else_post_page.open()
    else_post_page.open_menu()
    return else_post_page.make_repost()


@suite.register
class TestRepostElsePost(Auth):
    @seismograph.step(2, 'Test repost else post')
    def repost_else_post(self, browser):
        val = repost(browser)
        self.assertion.is_in(PUBLISHED, val)


@suite.register
class TestDoubleRepostElsePost(Auth):

    @seismograph.step(2, 'Test first repost else post')
    def first_double_repost_else_post(self, browser):
        val = repost(browser)
        self.assertion.is_in(PUBLISHED, val)

    @seismograph.step(3, 'Test second repost else post')
    def second_double_repost_else_post(self, browser):
        val = repost(browser)
        self.assertion.is_in(PUBLISHED, val)


@suite.register
class TestMakeFeedRepost(Auth):
    @seismograph.step(2, 'Test make feed repost')
    def make_feed_repost(self, browser):
        feed_page = FeedPage(browser)
        feed_page.get_popular_content()
        feed_page.open_menu_in_feed()
        val = feed_page.make_repost()
        self.assertion.is_in(PUBLISHED, val)


@suite.register
class TestRepostFeedAndDelete(Auth):
    @seismograph.step(2, 'Test make feed repost')
    def make_feed_repost(self, browser):
        feed_page = FeedPage(browser)
        feed_page.get_popular_content()
        feed_page.open_menu_in_feed()
        val = feed_page.make_repost()
        self.assertion.is_in(PUBLISHED, val)

    @seismograph.step(3, 'Test delete repost')
    def repost_feed_and_delete(self, browser):
        profile_page = ProfilePage(browser)
        profile_page.open()
        val = profile_page.delete_my_post()
        self.assertion.is_in(HIDDEN, val)

