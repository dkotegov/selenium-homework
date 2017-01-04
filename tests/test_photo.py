import seismograph
from seismograph.ext import selenium

from pages.auth_page import AuthPage
from pages.feed_page import FeedPage
from pages.photo_page import PhotoPage
from pages.album_page import AlbumPage
from utils.credentials import LOGIN, PASSWORD
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
        auth_page.auth(LOGIN, PASSWORD)


class BaseTestGotoPhoto(AuthStep):
    @seismograph.step(2, 'Test goto photo')
    def goto_photo(self, browser):
        feed_page = FeedPage(browser)
        feed_page.goto_photo()
        self.assertion.true(feed_page.photo_check.exist)


@suite.register
class TestGotoPhoto(BaseTestGotoPhoto):
    pass


@suite.register
class TestOpenAlbum(BaseTestGotoPhoto):
    @seismograph.step(3, 'Test open album')
    def open_album(self, browser):
        photo_page = PhotoPage(browser)
        photo_page.open_first_album()
        self.assertion.true(photo_page.check_opened_album.exist)


@suite.register
class TestCreateAlbum(BaseTestGotoPhoto):
    @seismograph.step(3, 'Test create album')
    def create_album(self, browser):
        photo_page = PhotoPage(browser)
        album_name = string_generator()
        photo_page.create_album(album_name)
        self.assertion.text_exist(photo_page.album_name, album_name)


class BaseTestOpenPhoto(BaseTestGotoPhoto):
    @seismograph.step(3, 'Test open photo')
    def open_photo(self, browser):
        self.photo_page = PhotoPage(browser)
        self.photo_page.open_first_photo()
        self.assertion.true(self.photo_page.close_button.exist)


@suite.register
class TestOpenPhoto(BaseTestOpenPhoto):
    pass


@suite.register
class TestClosePhoto(BaseTestOpenPhoto):
    @seismograph.step(4, 'Test close photo')
    def close_photo(self, browser):
        self.photo_page.close_photo()
        self.assertion.false(self.photo_page.close_button.is_displayed())


@suite.register
class TestRotatePhoto(BaseTestOpenPhoto):
    @seismograph.step(4, 'Test rotate photo')
    def rotate_photo(self, browser):
        self.assertion.true(self.photo_page.rotate_photo())


@suite.register
class TestDeleteRestorePhoto(BaseTestOpenPhoto):
    @seismograph.step(4, 'Test delete and restore photo')
    def delete_restore_photo(self, browser):
        self.photo_page.delete_restore_photo()
        self.assertion.true(self.photo_page.photo.exist)


@suite.register
class TestDeleteAlbum(BaseTestGotoPhoto):
    @seismograph.step(3, 'Test delete album')
    def delete_album(self, browser):
        album_page = AlbumPage(browser)
        album_page.delete_album()
        self.assertion.true(album_page.add_album.exist)


@suite.register
class TestNextPhoto(BaseTestOpenPhoto):
    @seismograph.step(4, 'Text next photo')
    def next_photo(self, browser):
        self.photo_page.next_photo()
        self.assertion.equal(self.photo_page.prev_size, self.photo_page.photo.size)
