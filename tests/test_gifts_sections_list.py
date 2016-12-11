# coding=utf-8
import seismograph
from seismograph.ext import selenium
from pages.auth_page import AuthPage
from pages.gifts_page import GiftsPage
from utils.auth_manager import AuthManager

suite = selenium.Suite(__name__)

ACTUAL_SECTION_LINK_SELECTOR_NAME = 'actual_section_link'


class AuthStep(selenium.Case):
    @seismograph.step(1, 'Login to ok.ru')
    def auth(self, browser):
        print 'AuthStep'
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
class TestActualSection(AuthStep, OpenPageStep, selenium.Case):
    @seismograph.step(3, 'Assert url and portlet name is valid')
    def check_section(self, browser):
        print 'TestActualSection - check_section'
        gifts_page = GiftsPage(browser)
        gifts_page.open()
        gifts_page.open_section(ACTUAL_SECTION_LINK_SELECTOR_NAME)
        gifts_page.gifts_portlet.wait()
        portlet_name_div = gifts_page.get_portlet_name()
        print browser.current_url
        print portlet_name_div.text
        self.assertion.is_in('/gifts', browser.current_url, 'URLI NE SOVPADAUT!')
        self.assertion.equal(portlet_name_div.text, u'Акция!')
