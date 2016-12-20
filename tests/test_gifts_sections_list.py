# coding=utf-8
import seismograph
from seismograph.ext import selenium

from pages.auth_page import AuthPage
from pages.gifts_page import GiftsPage
from utils.auth_manager import AuthManager

suite = selenium.Suite(__name__)

ACTUAL_SECTION_LINK_SELECTOR_NAME = 'actual_section_link'
AUTHOR_SECTION_LINK_SELECTOR_NAME = 'author_section_link'
POSTCARDS_SECTION_LINK_SELECTOR_NAME = 'postcards_section_link'
LOVE_SECTION_LINK_SELECTOR_NAME = 'love_section_link'
FRIEND_SECTION_LINK_SELECTOR_NAME = 'friend_section_link'
FLOWER_SECTION_LINK_SELECTOR_NAME = 'flower_section_link'
COMPLIMENTS_SECTION_LINK_SELECTOR_NAME = 'compliments_section_link'
MUSIC_SECTION_LINK_SELECTOR_NAME = 'music_section_link'
DESIGNER_SECTION_LINK_SELECTOR_NAME = 'designer_section_link'
MY_SECTION_LINK_SELECTOR_NAME = 'my_section_link'


class AuthStep(selenium.Case):
    @seismograph.step(1, 'Login to ok.ru')
    def auth(self, browser):
        print '\nAuthStep'
        auth_page = AuthPage(browser)
        auth_page.open()
        auth_page.auth(AuthManager.get_login(), AuthManager.get_password())


class OpenPageStep(selenium.Case):
    @seismograph.step(2, 'Open page')
    def auth(self, browser):
        print 'OpenPageStep'
        gifts_page = GiftsPage(browser)
        gifts_page.gifts_portlet.wait()


@suite.register
class TestAuthorSection(AuthStep, OpenPageStep, selenium.Case):
    @seismograph.step(3, 'Assert url and portlet name is valid')
    def check_section(self, browser):
        print 'TestAuthorSection - check_section'
        gifts_page = GiftsPage(browser)
        gifts_page.open()
        gifts_page.open_section(AUTHOR_SECTION_LINK_SELECTOR_NAME)
        portlet_name_div = gifts_page.get_portlet_name()
        print browser.current_url
        print portlet_name_div.text
        self.assertion.is_in('/gifts/authorGifts', browser.current_url, 'URLI NE SOVPADAUT!')
        self.assertion.equal(portlet_name_div.text, u'Подарки от пользователей')


@suite.register
class TestPostcardsSection(AuthStep, OpenPageStep, selenium.Case):
    @seismograph.step(3, 'Assert url and portlet name is valid')
    def check_section(self, browser):
        print 'TestPostcardsSection - check_section'
        gifts_page = GiftsPage(browser)
        gifts_page.open()
        gifts_page.open_section(POSTCARDS_SECTION_LINK_SELECTOR_NAME)
        portlet_name_div = gifts_page.get_portlet_name()
        print browser.current_url
        print portlet_name_div.text
        self.assertion.is_in('/gifts/liveGifts', browser.current_url, 'URLI NE SOVPADAUT!')
        self.assertion.equal(portlet_name_div.text, u'Открытки')


@suite.register
class TestLoveSection(AuthStep, OpenPageStep, selenium.Case):
    @seismograph.step(3, 'Assert url and portlet name is valid')
    def check_section(self, browser):
        print 'TestLoveSection - check_section'
        gifts_page = GiftsPage(browser)
        gifts_page.open()
        gifts_page.open_section(LOVE_SECTION_LINK_SELECTOR_NAME)
        portlet_name_div = gifts_page.get_portlet_name()
        print browser.current_url
        print portlet_name_div.text
        self.assertion.is_in('/gifts/searchBased1', browser.current_url, 'URLI NE SOVPADAUT!')
        self.assertion.equal(portlet_name_div.text, u'Любовь')


@suite.register
class TestFriendSection(AuthStep, OpenPageStep, selenium.Case):
    @seismograph.step(3, 'Assert url and portlet name is valid')
    def check_section(self, browser):
        print 'TestFriendSection - check_section'
        gifts_page = GiftsPage(browser)
        gifts_page.open()
        gifts_page.open_section(FRIEND_SECTION_LINK_SELECTOR_NAME)
        portlet_name_div = gifts_page.get_portlet_name()
        print browser.current_url
        print portlet_name_div.text
        self.assertion.is_in('/gifts/searchBased2', browser.current_url, 'URLI NE SOVPADAUT!')
        self.assertion.equal(portlet_name_div.text, u'Дружба')


@suite.register
class TestFlowerSection(AuthStep, OpenPageStep, selenium.Case):
    @seismograph.step(3, 'Assert url and portlet name is valid')
    def check_section(self, browser):
        print 'TestFlowerSection - check_section'
        gifts_page = GiftsPage(browser)
        gifts_page.open()
        gifts_page.open_section(FLOWER_SECTION_LINK_SELECTOR_NAME)
        portlet_name_div = gifts_page.get_portlet_name()
        print browser.current_url
        print portlet_name_div.text
        self.assertion.is_in('/gifts/searchBased3', browser.current_url, 'URLI NE SOVPADAUT!')
        self.assertion.equal(portlet_name_div.text, u'Цветы')


@suite.register
class TestComplimentsSection(AuthStep, OpenPageStep, selenium.Case):
    @seismograph.step(3, 'Assert url and portlet name is valid')
    def check_section(self, browser):
        print 'TestComplimentsSection - check_section'
        gifts_page = GiftsPage(browser)
        gifts_page.open()
        gifts_page.open_section(COMPLIMENTS_SECTION_LINK_SELECTOR_NAME)
        portlet_name_div = gifts_page.get_portlet_name()
        print browser.current_url
        print portlet_name_div.text
        self.assertion.is_in('/gifts/searchBased4', browser.current_url, 'URLI NE SOVPADAUT!')
        self.assertion.equal(portlet_name_div.text, u'Комплименты')


@suite.register
class TestMusicSection(AuthStep, OpenPageStep, selenium.Case):
    @seismograph.step(3, 'Assert url and portlet name is valid')
    def check_section(self, browser):
        print 'TestMusicSection - check_section'
        gifts_page = GiftsPage(browser)
        gifts_page.open()
        gifts_page.open_section(MUSIC_SECTION_LINK_SELECTOR_NAME)
        portlet_name_div = gifts_page.get_portlet_name()
        print browser.current_url
        print portlet_name_div.text
        self.assertion.is_in('/gifts/music', browser.current_url, 'URLI NE SOVPADAUT!')
        self.assertion.equal(portlet_name_div.text, u'Музыкальные подарки')


@suite.register
class TestDesignerSection(AuthStep, OpenPageStep, selenium.Case):
    @seismograph.step(3, 'Assert url and portlet name is valid')
    def check_section(self, browser):
        print 'TestDesignerSection - check_section'
        gifts_page = GiftsPage(browser)
        gifts_page.open()
        gifts_page.open_section(DESIGNER_SECTION_LINK_SELECTOR_NAME)
        portlet_name_div = gifts_page.get_portlet_name()
        print browser.current_url
        print portlet_name_div.text
        self.assertion.is_in('/gifts/designer', browser.current_url, 'URLI NE SOVPADAUT!')
        self.assertion.equal(portlet_name_div.text, u'Подарки ОК')


@suite.register
class TestMySection(AuthStep, OpenPageStep, selenium.Case):
    @seismograph.step(3, 'Assert url and portlet name is valid')
    def check_section(self, browser):
        print 'TestMySection - check_section'
        gifts_page = GiftsPage(browser)
        gifts_page.open()
        gifts_page.open_section(MY_SECTION_LINK_SELECTOR_NAME)
        portlet_name_div = gifts_page.get_portlet_name()
        print browser.current_url
        print portlet_name_div.text
        self.assertion.is_in('/gifts/my', browser.current_url, 'URLI NE SOVPADAUT!')
        self.assertion.equal(portlet_name_div.text, u'Отправленные')
