# -*- coding: utf-8 -*-

import seismograph
from seismograph.ext import selenium
from pages.auth_page import AuthPage
from pages.feed_page import FeedPage
from pages.profile_page import ProfilePage
from utils.auth_manager import AuthManager

suite = selenium.Suite(__name__)

TEST_PROFILE_ID = '570965759077'

DEFAULT_COST = u'100'
COST_1 = u'60'
COST_2 = u'50'


class AuthStep(selenium.Case):
    """Базовый класс со степом входа в ok.ru"""
    @seismograph.step(1, 'Login to ok.ru')
    def auth(self, browser):
        auth_page = AuthPage(browser)
        auth_page.open()
        auth_page.auth(AuthManager.get_login(),
                       AuthManager.get_password())


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
