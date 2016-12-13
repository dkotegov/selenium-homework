import seismograph
from seismograph.ext import selenium

from pages.auth_page import AuthPage
from pages.feed_page import FeedPage
from pages.photo_page import PhotoPage
from utils.auth_manager import AuthManager
import string
import random

def string_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

suite = seismograph.Suite(__name__, require=['selenium'])


class AuthStep(selenium.Case):
    @seismograph.step(1, 'Login to ok.ru')
    def auth(self, browser):
        auth_page = AuthPage(browser)
        auth_page.open()
        auth_page.auth(AuthManager.get_login(),
                       AuthManager.get_password())


@suite.register
class TestGotoPhoto(AuthStep, selenium.Case):
    @seismograph.step(2, 'Test goto photo')
    def goto_photo(self, browser):
        feed_page = FeedPage(browser)
        assert feed_page.goto_photo()


@suite.register
class TestOpenAlbum(AuthStep, selenium.Case):
    @seismograph.step(2, 'Test open album')
    def goto_photo(self, browser):
        feed_page = FeedPage(browser)
        feed_page.goto_photo()
        photo_page = PhotoPage(browser)
        assert photo_page.open_first_album()


@suite.register
class TestCreateAlbum(AuthStep, selenium.Case):
    @seismograph.step(2, 'Test create album')
    def create_album(self, browser):
        feed_page = FeedPage(browser)
        feed_page.goto_photo()
        photo_page = PhotoPage(browser)
        album_name = string_generator();
        self.assertion.text_exist(photo_page.create_album(album_name), album_name)