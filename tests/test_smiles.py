# -*- coding: utf-8 -*-

import seismograph
from seismograph.ext import selenium
from pages.feed_page import FeedPage
from tests.common_steps import AuthStep

suite = selenium.Suite(__name__)

DEFAULT_COST = u'60'
COST_1 = u'20'
COST_2 = u'50'


@suite.register
class TestSmilesAvailableFromToolbar(AuthStep, selenium.Case):
    """Дуступна ли покупка смайликов и стикеров из меню платных функций"""

    @seismograph.step(2, 'Check is smiles available from the paid functions menu')
    def check_is_available(self, browser):
        feed_page = FeedPage(browser)
        feed_page.open()
        feed_page.open_toolbar_dropdown()
        feed_page.open_payments_from_dropdown()
        feed_page.switch_to_last_frame()
        feed_page.click_paid_functions()
        assert feed_page.is_smiles_available_in_paid_functions()


@suite.register
class TestSmilesChangeCost(AuthStep, selenium.Case):
    """Меняется сумма при нажатии на нужный радио баттон в модальном окне покупки"""

    @seismograph.step(2, 'Check is smiles iframe changes cost')
    def check_is_cost_change(self, browser):
        feed_page = FeedPage(browser)
        feed_page.open()
        feed_page.open_payment_dropdown()
        feed_page.open_smiles_payment_from_dropdown()
        feed_page.switch_to_last_frame()
        cost = feed_page.get_smiles_cost()
        assert cost == DEFAULT_COST
        feed_page.click_smiles_checkbox_by_index(1)
        cost = feed_page.get_smiles_cost()
        assert cost == COST_1
        feed_page.click_smiles_checkbox_by_index(3)
        cost = feed_page.get_smiles_cost()
        assert cost == COST_2


@suite.register
class TestSmilesPaymentAvailable(AuthStep, selenium.Case):
    """Доступность покупки функции покупки смайликов и стикеров из дропдауна платных функций"""

    @seismograph.step(2, 'Check is smiles payment available from dropdown')
    def check_is_available(self, browser):
        feed_page = FeedPage(browser)
        feed_page.open()
        feed_page.open_payment_dropdown()
        feed_page.open_smiles_payment_from_dropdown()
        assert feed_page.is_payment_iframe_open()
