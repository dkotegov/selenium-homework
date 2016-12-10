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


class OpenPageStep(selenium.Case):
    @seismograph.step(2, 'Open page')
    def auth(self, browser):
        feed_page = FeedPage(browser)
        # feed_page.open()
        feed_page.avatar.wait(5)


@suite.register
class TestPaymentModal(AuthStep, OpenPageStep, selenium.Case):
    @seismograph.step(3, 'Assert modal is opened')
    def check_modal_opens(self, browser):
        feed_page = FeedPage(browser)
        payment_modal = feed_page.payment_modal()
        payment_modal.open()
        self.assertion.true(payment_modal.is_open())

    @seismograph.step(4, 'Close modal')
    def check_modal_closes(self, browser):
        feed_page = FeedPage(browser)
        payment_modal = feed_page.payment_modal()
        payment_modal.close()
        self.assertion.web_element_not_exist(browser, payment_modal.iframe)


@suite.register
class TestTransactions(AuthStep, OpenPageStep, selenium.Case):
    @seismograph.step(3, 'Open tab "Transactions"')
    def check_open(self, browser):
        feed_page = FeedPage(browser)
        payment_modal = feed_page.payment_modal()
        payment_modal.open()
        payment_modal.open_tab_transactions()
        self.assertion.web_element_exist(browser, payment_modal.get_tab_transaction())


@suite.register
class TestMyServices(AuthStep, OpenPageStep, selenium.Case):
    @seismograph.step(3, 'Open tab "My services"')
    def check_open(self, browser):
        feed_page = FeedPage(browser)
        payment_modal = feed_page.payment_modal()
        payment_modal.open()
        payment_modal.open_tab_my_services()
        self.assertion.greater(len(payment_modal.get_tab_my_services_els().all()), 1)


@suite.register
class TestMyCards(AuthStep, OpenPageStep, selenium.Case):
    @seismograph.step(3, 'Open tab "My cards"')
    def check_open(self, browser):
        feed_page = FeedPage(browser)
        payment_modal = feed_page.payment_modal()
        payment_modal.open()
        payment_modal.open_tab_my_cards()
        self.assertion.text_exist(payment_modal.get_tab_my_cards_add(), u'Добавление карты')


@suite.register
class TestBankCard(AuthStep, OpenPageStep, selenium.Case):
    @seismograph.step(3, 'Open tab "Bank cards"')
    def check_open(self, browser):
        feed_page = FeedPage(browser)
        payment_modal = feed_page.payment_modal()
        payment_modal.open()
        payment_modal.open_tab_transactions()
        payment_modal.open_tab_bank_card()
        self.assertion.web_element_exist(browser, payment_modal.get_tab_bank_card_input())


@suite.register
class TestPhone(AuthStep, OpenPageStep, selenium.Case):
    @seismograph.step(3, 'Open tab "Phone"')
    def check_open(self, browser):
        feed_page = FeedPage(browser)
        payment_modal = feed_page.payment_modal()
        payment_modal.open()
        payment_modal.open_tab_transactions()
        payment_modal.open_tab_phone()
        self.assertion.web_element_exist(browser, payment_modal.get_tab_phone_input())
        self.assertion.web_element_exist(browser, payment_modal.get_tab_phone_select())
        self.assertion.greater(len(payment_modal.get_tab_phone_els().all()), 1)


@suite.register
class TestTerminal(AuthStep, OpenPageStep, selenium.Case):
    @seismograph.step(3, 'Open tab "Terminals"')
    def check_open(self, browser):
        feed_page = FeedPage(browser)
        payment_modal = feed_page.payment_modal()
        payment_modal.open()
        payment_modal.open_tab_transactions()
        payment_modal.open_tab_terminal()
        self.assertion.web_element_exist(browser, payment_modal.get_tab_terminal_select())
        self.assertion.greater(len(payment_modal.get_tab_terminal_els().all()), 1)


@suite.register
class TestEMoney(AuthStep, OpenPageStep, selenium.Case):
    @seismograph.step(3, 'Open tab "Electronic money"')
    def check_open(self, browser):
        feed_page = FeedPage(browser)
        payment_modal = feed_page.payment_modal()
        payment_modal.open()
        payment_modal.open_tab_transactions()
        payment_modal.open_tab_emoney()
        self.assertion.greater(len(payment_modal.get_tab_emoney_els().all()), 1)
