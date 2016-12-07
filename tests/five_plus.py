# -*- coding: utf-8 -*-

from seismograph.ext import selenium
from utils.auth_manager import AuthManager
from utils.auth_pages import AuthPage
from utils.profile_page import ProfilePage
from utils.feed_page import FeedPage


suite = selenium.Suite(__name__)

TEST_PROFILE_ID = '570965759077'


@suite.register
def test_fivre_plus_change_cost(case, browser):
    """Меняется сумма при нажатии на нужный радио баттон в модальном окне покупки"""
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.auth(AuthManager.get_login(),
                   AuthManager.get_password())
    feed_page = FeedPage(browser)
    feed_page.open()
    feed_page.open_payment_dropdown()
    feed_page.open_five_plus_payment_from_dropdown()


@suite.register
def test_five_plus_payment_available(case, browser):
    """Доступность покупки функции 5+"""
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.auth(AuthManager.get_login(),
                   AuthManager.get_password())
    feed_page = FeedPage(browser)
    feed_page.open()
    feed_page.open_payment_dropdown()
    feed_page.open_five_plus_payment_from_dropdown()
    case.assertion.true(feed_page.is_five_plus_payment_open())


@suite.register
def test_add_five_plus_for_photo(case, browser):
    """Проставляется оценка 5+ при нажатии на 5+ под фотографией"""
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.auth(AuthManager.get_login(),
                   AuthManager.get_password())
    profile_page = ProfilePage(browser)
    profile_page.open(id=TEST_PROFILE_ID)
    profile_page.open_avatar()
    case.assertion.true(profile_page.is_five_plus_visible())


@suite.register
def test_open_five_plus_payment_from_photo(case, browser):
    """Открытие модального окна с покупкой при нажатии на 5+ под фотографией"""
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.auth(AuthManager.get_login(),
                   AuthManager.get_password())
    profile_page = ProfilePage(browser)
    profile_page.open(id=TEST_PROFILE_ID)
    profile_page.open_avatar()
    profile_page.open_five_plus_payment_from_photo()
    case.assertion.true(profile_page.is_five_plus_payment_open())



