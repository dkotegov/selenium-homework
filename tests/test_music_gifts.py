# coding=utf-8
import seismograph
from seismograph.ext import selenium

from pages.auth_page import AuthPage
from pages.gifts_page import GiftsPage
from utils.auth_manager import AuthManager

suite = selenium.Suite(__name__)


class AuthStep(selenium.Case):
    @seismograph.step(1, 'Login to ok.ru')
    def auth(self, browser):
        # print '\nAuthStep'
        auth_page = AuthPage(browser)
        auth_page.open()
        auth_page.auth(AuthManager.get_login(), AuthManager.get_password())


class OpenPageStep(selenium.Case):
    @seismograph.step(2, 'Open page')
    def auth(self, browser):
        # print 'OpenPageStep'
        gifts_page = GiftsPage(browser)
        gifts_page.gifts_portlet.wait()


@suite.register
class TestMusicGiftsBehavior(AuthStep, OpenPageStep, selenium.Case):
    @seismograph.step(3, 'Assert music in gifts works')
    def check_music_appearance(self, browser):
        # print 'TestMusicGiftsBehavior - check_music_appearance'
        gifts_page = GiftsPage(browser)
        gifts_page.open()
        gifts_page.open_music_tab()
        first_selectable_song = gifts_page.get_first_selectable_song()
        artist = first_selectable_song.get_attribute('data-artist')
        gifts_page.choose_first_song()
        title = gifts_page.get_selected_song_title().text
        # print title
        # print artist
        self.assertion.true(title.startswith(artist))
