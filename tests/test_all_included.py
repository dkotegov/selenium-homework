# -*- coding: utf-8 -*-
import seismograph
from seismograph.ext import selenium
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait

from test_invisible_mode import LeftColumnTopCardUser
from test_invisible_mode import WebOkSuite
from test_invisible_mode import click_element

suite = seismograph.Suite(__name__, require=['selenium'])


class MiddleColumnTopCardUser(selenium.Page):
    friend_ref = selenium.PageElement(
        selenium.query(
            selenium.query.A,
            _class='mctc_navMenuSec',
        ),
    )


@suite.register
class BuyAllPresents(WebOkSuite, selenium.Case):
    @seismograph.step(2, 'Buy all included mode')
    def check_text(self, browser):
        user_card = LeftColumnTopCardUser()
        WebDriverWait(browser, 3).until(
            lambda br: LeftColumnTopCardUser(br).invisible_toggler.first()
        )
        try:
            browser.execute_script(click_element(user_card.check_all_included))
            browser.execute_script(click_element(user_card.choose_month_subscr))
            browser.execute_script(click_element(user_card.click_buy_btn))
            browser.execute_script(click_element(user_card.close_modal_window))
        except (AttributeError, WebDriverException):
            assert True
            print 'All included mode is already bought'
        except Exception:
            assert False
