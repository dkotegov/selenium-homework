# coding=utf-8
import seismograph
from seismograph.ext import selenium

from pages.auth_page import AuthPage
from pages.gifts_page import GiftsPage
from utils.auth_manager import AuthManager

suite = selenium.Suite(__name__)

GIFT_BLOCK_SELECTOR_NAME = 'gift_block'
GIFT_SELECTOR_NAME = 'gift'


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
class TestProgressiveScroll(AuthStep, OpenPageStep, selenium.Case):
    @seismograph.step(3, 'Assert progressive scroll is works')
    def check_one_scroll(self, browser):
        # print 'TestProgressiveScroll - check_one_scroll'
        gifts_page = GiftsPage(browser)
        gifts_page.open()
        gift_blocks_count_before_scroll = gifts_page.get_gifts_block_count()
        gift_count_before_scroll = gifts_page.get_gifts_count()
        gifts_page.scroll_to_page_down()
        gift_blocks_count_after_scroll = gifts_page.get_gifts_block_count()
        gift_count_after_scroll = gifts_page.get_gifts_count()
        # print gift_blocks_count_before_scroll, gift_blocks_count_after_scroll
        # print gift_count_before_scroll, gift_count_after_scroll
        self.assertion.true(gift_blocks_count_before_scroll < gift_blocks_count_after_scroll)
        self.assertion.true(gift_count_before_scroll < gift_count_after_scroll)

    @seismograph.step(3, 'Assert progressive scroll is works')
    def check_many_scrolls(self, browser):
        # print 'TestProgressiveScroll - check_many_scrolls'
        gifts_page = GiftsPage(browser)
        gifts_page.open()
        gift_blocks_count_before_scroll = gifts_page.get_gifts_block_count()
        gift_count_before_scroll = gifts_page.get_gifts_count()
        gifts_page.scroll_to_page_down()
        gifts_page.scroll_to_page_down()
        gifts_page.scroll_to_page_down()
        gifts_page.scroll_to_page_down()
        gifts_page.scroll_to_page_down()
        gifts_page.scroll_to_page_down()
        gifts_page.scroll_to_page_down()
        gifts_page.scroll_to_page_down()
        gifts_page.scroll_to_page_down()
        gifts_page.scroll_to_page_down()
        gift_blocks_count_after_scroll = gifts_page.get_gifts_block_count()
        gift_count_after_scroll = gifts_page.get_gifts_count()
        # print gift_blocks_count_before_scroll, gift_blocks_count_after_scroll
        # print gift_count_before_scroll, gift_count_after_scroll
        self.assertion.true(gift_blocks_count_before_scroll < gift_blocks_count_after_scroll)
        self.assertion.true(gift_count_before_scroll < gift_count_after_scroll)
