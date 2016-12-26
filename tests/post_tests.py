# coding=utf-8
import seismograph
from seismograph.ext import selenium
from pages.auth_page import AuthPage
from pages.group_page import PostPage
from pages.profile_page import ProfilePage
from pages.feed_page import FeedPage
from smth.auth import AuthManager


suite = selenium.Suite(__name__)


class Auth(selenium.Case):

    @seismograph.step(1, 'Auth')
    def auth(self, browser):
        auth_page = AuthPage(browser)
        auth_page.open()
        auth_page.auth(AuthManager.get_login(),
                       AuthManager.get_password())


@suite.register
class TestPost(Auth, selenium.Case):

    @seismograph.step(2, 'Test post')
    def post(self, browser):
        text = 'Test number 1'
        feed_page = FeedPage(browser)
        feed_page.show_post()

        post_page = PostPage(browser)
        post_page.wait_overlay()
        post_page.create_post(text)

        profile_page = ProfilePage(browser)
        profile_page.open()
        self.assertion.is_in(text, profile_page.get_first_post())


@suite.register
class TestDeletePost(Auth, selenium.Case):

    @seismograph.step(2, 'Test post and delete')
    def post_and_delete(self, browser):
        text = 'Test number 2'
        feed_page = FeedPage(browser)
        feed_page.show_post()

        post_page = PostPage(browser)
        post_page.wait_overlay()
        post_page.create_post(text)

        profile_page = ProfilePage(browser)
        profile_page.open()
        self.assertion.is_in(text, profile_page.get_first_post())
        self.assertion.is_in(u'скрыто', profile_page.delete_my_post())
