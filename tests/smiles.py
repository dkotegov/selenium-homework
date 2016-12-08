# -*- coding: utf-8 -*-

from seismograph.ext import selenium
from pages.auth_pages import AuthPage
from pages.feed_page import FeedPage
from pages.profile_page import ProfilePage
from utils.auth_manager import AuthManager

suite = selenium.Suite(__name__)


DEFAULT_COST = u'60'
COST_1 = u'20'
COST_2 = u'50'


@suite.register
def test_smiles_available_from_toolbar(case, browser):
    """Дуступна ли покупка смайликов и стикеров из меню платных функций"""
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.auth(AuthManager.get_login(),
                   AuthManager.get_password())
    feed_page = FeedPage(browser)
    feed_page.open()
    feed_page.open_toolbar_dropdown()
    feed_page.open_payments_from_dropdown()
    feed_page.switch_to_last_frame()
    feed_page.click_paid_functions()
    case.assertion.true(feed_page.is_smiles_available_in_paid_functions())


@suite.register
def test_smiles_change_cost(case, browser):
    """Меняется сумма при нажатии на нужный радио баттон в модальном окне покупки"""
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.auth(AuthManager.get_login(),
                   AuthManager.get_password())
    feed_page = FeedPage(browser)
    feed_page.open()
    feed_page.open_payment_dropdown()
    feed_page.open_smiles_payment_from_dropdown()
    feed_page.switch_to_last_frame()
    cost = feed_page.get_smiles_cost()
    case.assertion.equal(cost, DEFAULT_COST)
    feed_page.click_smiles_checkbox_by_index(1)
    cost = feed_page.get_smiles_cost()
    case.assertion.equal(cost, COST_1)
    feed_page.click_smiles_checkbox_by_index(3)
    cost = feed_page.get_smiles_cost()
    case.assertion.equal(cost, COST_2)


@suite.register
def test_smiles_payment_available(case, browser):
    """Доступность покупки функции покупки смайликов и стикеров из дропдауна платных функций"""
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.auth(AuthManager.get_login(),
                   AuthManager.get_password())
    feed_page = FeedPage(browser)
    feed_page.open()
    feed_page.open_payment_dropdown()
    feed_page.open_smiles_payment_from_dropdown()
    case.assertion.true(feed_page.is_payment_iframe_open())




