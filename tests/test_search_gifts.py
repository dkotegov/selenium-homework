# coding=utf-8
import random
import string

import seismograph
import time
from seismograph.ext import selenium
from pages.auth_page import AuthPage
from pages.gifts_page import GiftsPage
from utils.auth_manager import AuthManager

suite = selenium.Suite(__name__)

GIFT_SELECTOR_NAME = 'gift'
MORE_SLASH_QUERY = '////////////////'
DOTS_AND_COMMAS_AND_SEMICOLONS_QUERY = '.,.,.,.,.,.,.,.,.,;;;;'
UNDERSCORE_QUERY = '_______________'


def rand_str(n):
    return ''.join([random.choice(string.lowercase) for i in xrange(n)])


class AuthStep(selenium.Case):
    @seismograph.step(1, 'Login to ok.ru')
    def auth(self, browser):
        print '\nAuthStep'
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
class TestSearchSymbolsQueries(AuthStep, OpenPageStep, selenium.Case):
    @seismograph.step(3, 'Assert searching works')
    def check_more_slash_query_search(self, browser):
        print 'TestProgressiveScroll - check_more_slash_query_search'
        gifts_page = GiftsPage(browser)
        gifts_page.open()
        gifts_page.search(MORE_SLASH_QUERY)
        gift_count = gifts_page.get_gifts_count()
        self.assertion.equal(gift_count, 0)

    @seismograph.step(3, 'Assert searching works')
    def check_dots_and_commas_and_semicolons_query_search(self, browser):
        print 'TestProgressiveScroll - check_dots_and_commas_and_semicolons_query_search'
        gifts_page = GiftsPage(browser)
        gifts_page.open()
        gifts_page.search(DOTS_AND_COMMAS_AND_SEMICOLONS_QUERY)
        gift_count = gifts_page.get_gifts_count()
        self.assertion.equal(gift_count, 0)

    @seismograph.step(3, 'Assert searching works')
    def check_underscore_query_search(self, browser):
        print 'TestProgressiveScroll - check_underscore_query_search'
        gifts_page = GiftsPage(browser)
        gifts_page.open()
        gifts_page.search(UNDERSCORE_QUERY)
        gift_count = gifts_page.get_gifts_count()
        self.assertion.equal(gift_count, 0)


@suite.register
class TestSearchRandomQueries(AuthStep, OpenPageStep, selenium.Case):
    @seismograph.step(3, 'Assert searching works with random queries')
    def check_random_query_search(self, browser):
        print 'TestProgressiveScroll - check_random_query_search'
        gifts_page = GiftsPage(browser)
        gifts_page.open()
        gifts_page.search(rand_str(25))
        gift_count = gifts_page.get_gifts_count()
        self.assertion.equal(gift_count, 0)
