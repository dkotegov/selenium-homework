# coding=utf-8
import seismograph
import time
from seismograph.ext import selenium
from pages.auth_page import AuthPage
from pages.feed_page import FeedPage
from utils.auth_manager import AuthManager

suite = selenium.Suite(__name__)


class AuthStep(selenium.Case):
    @seismograph.step(1, 'Login to ok.ru')
    def auth(self, browser):
        auth_page = AuthPage(browser)
        auth_page.open()
        auth_page.auth(AuthManager.get_login(),
                       AuthManager.get_password())


#@suite.register
class TestBuyOksModal(AuthStep, selenium.Case):
    @seismograph.step(2, 'Open modal')
    def check_modal_opens(self, browser):
        feed_page = FeedPage(browser)
        feed_page.open()
        feed_page.avatar.wait()
        feed_page.open_payment_modal()
        self.assertion.true(feed_page.is_payment_modal_open())

    @seismograph.step(3, 'Close modal')
    def check_modal_closes(self, browser):
        feed_page = FeedPage(browser)
        feed_page.close_payment_modal()
        self.assertion.web_element_not_exist(browser, feed_page.payment_iframe)


# @suite.register
# class TestAddCard(AuthStep, selenium.Case):
#     @seismograph.step(2, 'Try to add card')
#     def check_wrong_card_error(self, browser):
#         feed_page = FeedPage(browser)
#         feed_page.open()
#         feed_page.avatar.wait()
#         feed_page.open_payment_modal()
#         time.sleep(10)
