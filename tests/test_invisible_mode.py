# -*- coding: utf-8 -*-
import seismograph
from seismograph.ext import selenium
from selenium.webdriver.support.wait import WebDriverWait

from tests.common_steps import AuthStep
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
    text_turn_down_invisible = u"Выключить невидимку"

    check_invisible_mode = \
        'document.getElementById("hook_Block_LeftColumnTopCardUser")' \
        '.getElementsByTagName("ul")[1].getElementsByTagName("li")[8]' \
        '.getElementsByTagName("a")[0]'

    invisible_text = selenium.PageElement(
        selenium.query(
            selenium.query.SPAN,
            _class="tico ",
        )
    )

    invisible_toggler = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            id="invisibleToggler",
            type="checkbox"
        ),
        action=lambda button: button.click(),
    )

    def wait_for_invisible_toggler(self):
        WebDriverWait(selenium.Page.browser, 3).until(
            lambda br: self.invisible_toggler.first()
        )


class LeftColumnTopCardUserMobile(selenium.Page):
    check_invisible_mode = 'document.getElementById("userInvisibleSettingItemCheckBox")'

    invisible_toggler = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            _class="tumbler_target nofasttouch js-ajax-checkbox",
        ),
    )

    def wait_for_invisible_toggler(self):
        WebDriverWait(selenium.Page.browser, 5).until(
            lambda br: self.invisible_toggler.first()
        )


class UpperNavbar(selenium.Page):
    click_user_settings_icon = \
        'document.getElementsByClassName("ucard-mini toolbar_ucard")[0]'

    check_invisible_mode = \
        'document.getElementsByClassName("toolbar_dropdown")[0]' \
        '.getElementsByTagName("ul")[0].getElementsByTagName("li")[3]' \
        '.getElementsByTagName("a")[0]'


class WebOkSuite(AuthStep):
    @seismograph.step(2, 'Setup invisible mode')
    def go_to_ok_registered(self, browser):
        user_card = LeftColumnTopCardUser(browser)
        user_card.wait_for_invisible_toggler()
        if user_card.invisible_toggler.is_selected():
            browser.execute_script(click_element(user_card.check_invisible_mode))
            browser.refresh()


@suite.register
class CheckInvisibleModeFromNavbar(WebOkSuite):
    @seismograph.step(3, 'Check invisible mode from navbar')
    def check_text(self, browser):
        user_card = LeftColumnTopCardUser(browser)
        user_card.wait_for_invisible_toggler()
        browser.execute_script(click_element(UpperNavbar.click_user_settings_icon))
        browser.execute_script(click_element(UpperNavbar.check_invisible_mode))
        user_card.wait_for_invisible_toggler()
        self.assertion.text_exist(browser, user_card.text_turn_down_invisible)

@suite.register
class CheckInvisibleModeFromMainPage(WebOkSuite):
    @seismograph.step(3, 'Check invisible from main page')
    def check_text(self, browser):
        user_card = LeftColumnTopCardUser(browser)
        user_card.wait_for_invisible_toggler()
        browser.execute_script(click_element(user_card.check_invisible_mode))
        browser.refresh()
        user_card.wait_for_invisible_toggler()
        self.assertion.text_exist(browser, user_card.text_turn_down_invisible)


@suite.register
class CheckInvisibleModeFromMobileVersion(selenium.Case):
    @seismograph.step(1, 'Login to m.ok.ru and setup invisible mode')
    def go_to_ok_registered(self, browser):
        browser.go_to('http://m.ok.ru/')
        morda = OkMobileMorda(browser)
        morda.email_input.send_keys(AuthManager.get_login())
        morda.password_input.send_keys(AuthManager.get_password())
        morda.submit_btn.first().click()

        user_card = LeftColumnTopCardUserMobile(browser)
        user_card.wait_for_invisible_toggler()
        if user_card.invisible_toggler.first().is_selected():
            browser.execute_script(click_element(user_card.check_invisible_mode))
            browser.refresh()

    @seismograph.step(2, 'Check invisible mode for mobile version')
    def check_text(self, browser):
        user_card = LeftColumnTopCardUserMobile(browser)
        browser.execute_script(click_element(user_card.check_invisible_mode))
        user_card.wait_for_invisible_toggler()
        browser.refresh()
        assert user_card.invisible_toggler.first().is_selected()
