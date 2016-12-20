# coding=utf-8
import seismograph
from seismograph.ext import selenium

from pages.auth_page import AuthPage
from pages.gifts_page import GiftsPage
from utils.auth_manager import AuthManager

suite = selenium.Suite(__name__)

GIFT_SELECTOR_NAME = 'gift'
AUTHOR_SECTION_LINK_SELECTOR_NAME = 'author_section_link'


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
class TestGiftTooltipBehavior(AuthStep, OpenPageStep, selenium.Case):
    @seismograph.step(3, 'Assert gifts tooltips works')
    def check_tooltip_appearance(self, browser):
        # print 'TestGiftTooltipBehavior - check_tooltip_appearance'
        gifts_page = GiftsPage(browser)
        gifts_page.open()
        gifts_page.open_section(AUTHOR_SECTION_LINK_SELECTOR_NAME)
        first_gift_element = gifts_page.get_first_gift()
        gifts_page.hack_move_mouse_to_element(first_gift_element)
        tooltips = gifts_page.get_tooltips()
        self.assertion.equal(len(tooltips), 1)
