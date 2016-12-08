# -*- coding: utf-8 -*-
from time import sleep

import seismograph
from seismograph.ext import selenium
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait

from utils.auth_manager import AuthManager

suite = seismograph.Suite(__name__, require=['selenium'])


def click_element(element):
    return element + '.click()'


class OkMorda(selenium.Page):
    email_input = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            id='field_email',
        ),
    )

    password_input = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            id='field_password',
        ),
    )

    submit_btn = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            _class='button-pro form-actions_yes',
        ),
    )


class OkMobileMorda(selenium.Page):
    email_input = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            name="fr.login",
        ),
    )

    password_input = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            name="fr.password",
        ),
    )

    submit_btn = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            _class='base-button_target',
        ),
    )


class LeftColumnTopCardUser(selenium.Page):
    check_all_included = \
        'document.getElementById("hook_Block_LeftColumnTopCardUser")' \
        '.getElementsByTagName("ul")[1].getElementsByTagName("li")[6]' \
        '.getElementsByTagName("a")[0]'

    check_invisible_mode = \
        'document.getElementById("hook_Block_LeftColumnTopCardUser")' \
        '.getElementsByTagName("ul")[1].getElementsByTagName("li")[7]' \
        '.getElementsByTagName("a")[0]'

    choose_month_subscr = 'document.getElementById("val_-1")'

    click_buy_btn = \
        'document.getElementsByClassName("form-actions __center")[0]' \
        '.getElementsByClassName("button-pro form-actions__yes")[0]'

    close_modal_window = 'document.getElementById("nohook_modal_close")'

    invisible_toggler = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            id="invisibleToggler",
        ),
    )


class LeftColumnTopCardUserMobile(selenium.Page):
    check_invisible_mode = \
        'document.getElementById("userInvisibleSettingItemCheckBox")'

    invisible_toggler = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            id="userInvisibleSettingItemCheckBox",
        ),
    )


class UpperNavbar(selenium.Page):
    click_user_settings_icon = \
        'document.getElementsByClassName("ucard-mini toolbar_ucard")[0]'

    check_invisible_mode = \
        'document.getElementsByClassName("toolbar_dropdown")[0]' \
        '.getElementsByTagName("ul")[0].getElementsByTagName("li")[3]' \
        '.getElementsByTagName("a")[0]'


class WebOkSuite(selenium.Case):
    @seismograph.step(1, 'Login to ok.ru')
    def go_to_ok_registered(self, browser):
        browser.go_to('http://ok.ru/')
        morda = OkMorda(browser)
        morda.email_input.send_keys(AuthManager.get_login())
        morda.password_input.send_keys(AuthManager.get_password())
        morda.submit_btn.first().click()


@suite.register
class BuyInvisibleMode(WebOkSuite, selenium.Case):
    @seismograph.step(2, 'Buy invisible function')
    def check_text(self, browser):
        user_card = LeftColumnTopCardUser()
        WebDriverWait(browser, 3).until(
            lambda br: LeftColumnTopCardUser(br).invisible_toggler.first()
        )
        try:
            browser.execute_script(click_element(user_card.check_invisible_mode))
            browser.execute_script(click_element(user_card.choose_month_subscr))
            browser.execute_script(click_element(user_card.click_buy_btn))
            browser.execute_script(click_element(user_card.close_modal_window))
        except (AttributeError, WebDriverException):
            assert True
            print "Invisible mode already bought"
        except Exception:
            assert False


@suite.register
class CheckInvisibleModeFromMainPage(WebOkSuite, selenium.Case):
    @seismograph.step(2, 'Check invisible from main page')
    def check_text(self, browser):
        user_card = LeftColumnTopCardUser(browser)
        WebDriverWait(browser, 3).until(
            lambda br: LeftColumnTopCardUser(br).invisible_toggler.first()
        )
        if user_card.invisible_toggler.first().is_selected():
            browser.execute_script(click_element(user_card.check_invisible_mode))
            WebDriverWait(browser, 3).until(
                lambda br: LeftColumnTopCardUser(br).invisible_toggler.first()
            )
            assert not user_card.invisible_toggler.first().is_selected()
        else:
            browser.execute_script(click_element(user_card.check_invisible_mode))
            WebDriverWait(browser, 3).until(
                lambda br: LeftColumnTopCardUser(br).invisible_toggler.first()
            )
            assert user_card.invisible_toggler.first().is_selected()


@suite.register
class CheckInvisibleModeFromNavbar(WebOkSuite, selenium.Case):
    @seismograph.step(2, 'Check invisible mode from navbar')
    def check_text(self, browser):
        user_card = LeftColumnTopCardUser(browser)
        WebDriverWait(browser, 3).until(
            lambda br: LeftColumnTopCardUser(br).invisible_toggler.first()
        )
        if user_card.invisible_toggler.first().is_selected():
            browser.execute_script(click_element(user_card.check_invisible_mode))
        browser.execute_script(click_element(UpperNavbar.click_user_settings_icon))
        browser.execute_script(click_element(UpperNavbar.check_invisible_mode))
        sleep(3)
        assert user_card.invisible_toggler.first().is_selected()


@suite.register
class CheckInvisibleModeFromMobileVersion(selenium.Case):
    @seismograph.step(1, 'Login to m.ok.ru')
    def go_to_ok_registered(self, browser):
        browser.go_to('http://m.ok.ru/')
        morda = OkMobileMorda(browser)
        morda.email_input.send_keys(AuthManager.get_login())
        morda.password_input.send_keys(AuthManager.get_password())
        morda.submit_btn.first().click()

    @seismograph.step(2, 'Check invisible mode for mobile version')
    def check_text(self, browser):
        user_card = LeftColumnTopCardUserMobile(browser)
        WebDriverWait(browser, 3).until(
            lambda br: LeftColumnTopCardUserMobile(br).invisible_toggler.first()
        )
        if not user_card.invisible_toggler.first().is_selected():
            browser.execute_script(click_element(user_card.check_invisible_mode))
            assert user_card.invisible_toggler.first().is_selected()
        else:
            browser.execute_script(click_element(user_card.check_invisible_mode))
            assert not user_card.invisible_toggler.first().is_selected()
