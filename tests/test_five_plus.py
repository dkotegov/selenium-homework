# -*- coding: utf-8 -*-

import seismograph
from seismograph.ext import selenium
from pages.feed_page import FeedPage
from pages.profile_page import ProfilePage
from tests.common_steps import AuthStep

suite = selenium.Suite(__name__)

TEST_PROFILE_ID = '570965759077'

DEFAULT_COST = u'100'
COST_1 = u'60'
COST_2 = u'50'


@suite.register
class TestFivePlusAvailableFromToolbar(AuthStep, selenium.Case):
    """Доступность покупки функции 5+ из меню платных функций"""

    @seismograph.step(2, 'Check is 5+ available')
    def check_is_available(self, browser):
        feed_page = FeedPage(browser)
        feed_page.open()
        feed_page.open_toolbar_dropdown()
        feed_page.open_payments_from_dropdown()
        feed_page.switch_to_last_frame()
        feed_page.click_paid_functions()
        assert feed_page.is_five_plus_available_in_paid_functions()


@suite.register
class TestFivePlusChangeCost(AuthStep, selenium.Case):
    """Меняется сумма при нажатии на нужный радио баттон в модальном окне покупки"""

    @seismograph.step(2, 'Check is 5+ iframe change cost')
    def check_is_change_cost(self, browser):
        feed_page = FeedPage(browser)
        feed_page.open()
        feed_page.open_payment_dropdown()
        feed_page.open_five_plus_payment_from_dropdown()
        feed_page.switch_to_last_frame()
        cost = feed_page.get_five_plus_cost()
        assert cost == DEFAULT_COST
        feed_page.click_five_plus_checkbox_by_index(1, COST_1)
        feed_page.switch_to_last_frame()
        cost = feed_page.get_five_plus_cost()
        assert cost == COST_1
        feed_page.click_five_plus_checkbox_by_index(2, COST_2)
        feed_page.switch_to_last_frame()
        cost = feed_page.get_five_plus_cost()
        assert cost == COST_2


@suite.register
class TestFivePlusPaymentAvailable(AuthStep, selenium.Case):
    """Доступность покупки функции 5+ из дропдауна платных функций"""

    @seismograph.step(2, 'Check is 5+ payment available from dropdown')
    def check_is_available(self, browser):
        feed_page = FeedPage(browser)
        feed_page.open()
        feed_page.open_payment_dropdown()
        feed_page.open_five_plus_payment_from_dropdown()
        assert feed_page.is_payment_iframe_open()


@suite.register
class TestAddFivePlusForPhoto(AuthStep, selenium.Case):
    """Проставляется оценка 5+ при нажатии на 5+ под фотографией"""

    @seismograph.step(2, 'Check is 5+ available under the photo')
    def check_is_available(self, browser):
        profile_page = ProfilePage(browser)
        profile_page.open(id=TEST_PROFILE_ID)
        profile_page.open_avatar()
        assert profile_page.is_five_plus_visible()


@suite.register
class TestOpenFivePlusPaymentFromPhoto(AuthStep, selenium.Case):
    """Открытие модального окна с покупкой при нажатии на 5+ под фотографией"""

    @seismograph.step(2, 'Check is 5+ iframe available from the photo')
    def check_is_available(self, browser):
        profile_page = ProfilePage(browser)
        profile_page.open(id=TEST_PROFILE_ID)
        profile_page.open_avatar()
        profile_page.open_five_plus_payment_from_photo()
        assert profile_page.is_five_plus_payment_open()
