# coding=utf-8
import seismograph
from seismograph.ext import selenium
from auth_test import Auth
from pages.feed_page import FeedPage
from pages.group_post_page import GroupPostPage


TOPIC = '/topic/'
COMMENT = 'comment'
PUBLIC_COMMENT = 'hmm...'
YOU = u'Вы'
KLASS = u'Класс'

suite = selenium.Suite(__name__)


@suite.register
class TestGetAuthorGroup(Auth):
    @seismograph.step(2, 'Test get author group')
    def get_author_group(self, browser):
        feed_page = FeedPage(browser)
        url = feed_page.get_author()
        feed_page.click_post_title()
        self.assertion.is_in(url, browser.current_url)


@suite.register
class TestGetPost(Auth):
    @seismograph.step(2, 'Test get post')
    def get_post(self, browser):
        feed_page = FeedPage(browser)
        feed_page.get_popular_content()
        url = feed_page.get_post()
        self.assertion.is_in(TOPIC, url)


@suite.register
class TestLikeOnOwnPost(Auth):
    @seismograph.step(2, 'Test like on own post')
    def like_on_own_post(self, browser):
        feed_page = FeedPage(browser)
        before = feed_page.get_own_post_like()
        after = feed_page.make_like_on_own_post(before)
        self.assertion.not_equal(before, after)


@suite.register
class TestMakeSelfComment(Auth):
    @seismograph.step(2, 'Test make self comment')
    def make_self_comment(self, browser):
        feed_page = FeedPage(browser)
        feed_page.click_status_comment()
        val = feed_page.make_self_comment(COMMENT)
        self.assertion.is_in(COMMENT, val)


@suite.register
class TestMakeComment(Auth):
    @seismograph.step(2, 'Test make comment')
    def make_comment(self, browser):
        feed_page = FeedPage(browser)
        feed_page.get_popular_content()
        feed_page.click_post_comment()
        val = feed_page.make_comment(PUBLIC_COMMENT)
        self.assertion.is_in(PUBLIC_COMMENT, val)


@suite.register
class TestMakeLikeOnSelfComment(Auth):
    @seismograph.step(2, 'Test make self comment')
    def make_self_comment(self, browser):
        feed_page = FeedPage(browser)
        feed_page.click_status_comment()
        val = feed_page.make_self_comment(COMMENT)
        self.assertion.is_in(COMMENT, val)

    @seismograph.step(3, 'Test make like on self comment')
    def make_like_on_self_comment(self, browser):
        feed_page = FeedPage(browser)
        text = feed_page.make_like_on_self_comment()
        self.assertion.equal(YOU, text)


@suite.register
class TestMakeDoubleLike(Auth):
    @seismograph.step(2, 'Test make self comment')
    def make_self_comment(self, browser):
        feed_page = FeedPage(browser)
        feed_page.click_status_comment()
        val = feed_page.make_self_comment(COMMENT)
        self.assertion.is_in(COMMENT, val)

    @seismograph.step(3, 'Test first like on self comment')
    def make_first_like_on_self_comment(self, browser):
        feed_page = FeedPage(browser)
        text = feed_page.make_like_on_self_comment()
        self.assertion.is_in(YOU, text)

    @seismograph.step(4, 'Test second like on self comment')
    def make_second_like_on_self_comment(self, browser):
        feed_page = FeedPage(browser)
        text = feed_page.make_like_on_self_comment(True)
        self.assertion.is_in(KLASS, text)


@suite.register
class TestMakeGroupComment(Auth):
    @seismograph.step(2, 'Test make group comment')
    def make_group_comment(self, browser):
        group_page = GroupPostPage(browser)
        group_page.open()
        group_page.open_post_comments()
        text = group_page.make_group_comment(PUBLIC_COMMENT)
        self.assertion.is_in(PUBLIC_COMMENT, text)


@suite.register
class TestMakeFeedLike(Auth):
    @seismograph.step(2, 'Test make feed like')
    def make_feed_like(self, browser):
        feed_page = FeedPage(browser)
        feed_page.get_popular_content()
        before = feed_page.get_feed_like()
        after = feed_page.make_feed_like(before)
        self.assertion.not_equal(before, after)
