# -*- coding: utf-8 -*-
import seismograph
from seismograph.ext import selenium
from selenium.webdriver.support.wait import WebDriverWait

from tests.common_steps import AuthStep
from utils.auth_manager import AuthManager

suite = seismograph.Suite(__name__, require=['selenium'])


class OkMobileMorda(selenium.Page):
    link = 'http://m.ok.ru/'

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
        '.getElementsByTagName("a")[0].click()'

    invisible_toggler = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            id="invisibleToggler",
            type="checkbox"
        ),
    )

    def wait_for_invisible_toggler(self):
        WebDriverWait(selenium.Page.browser, 3).until(
            lambda br: self.invisible_toggler.first()
        )


class LeftColumnTopCardUserMobile(selenium.Page):
    invisible_mode = 'document.getElementById("userInvisibleSettingItemCheckBox").click()'

    invisible_toggler = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            _class="tumbler_target nofasttouch js-ajax-checkbox",
        ),
    )

    def wait_for_invisible_toggler(self):
        WebDriverWait(selenium.Page.browser, 3).until(
            lambda br: self.invisible_toggler.first()
        )


class UpperNavbar(selenium.Page):
    click_user_settings_icon = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class='ucard-mini toolbar_ucard',
        )
    )

    invisible_mode = selenium.PageElement(
        selenium.query(
            selenium.query.SPAN,
            _class="u-menu_tx ellip-i"
        )
    )

    def check_invisible_mode(self):
        return self.invisible_mode.all()[3]


class WebOkSuite(AuthStep):
    @seismograph.step(2, 'Setup invisible mode')
    def go_to_ok_registered(self, browser):
        user_card = LeftColumnTopCardUser(browser)
        user_card.wait_for_invisible_toggler()
        if user_card.invisible_toggler.first().is_selected():
            browser.execute_script(user_card.check_invisible_mode)
            browser.refresh()


@suite.register
class CheckInvisibleModeFromNavbar(WebOkSuite):
    @seismograph.step(3, 'Check invisible mode from navbar')
    def check_text(self, browser):
        user_card = LeftColumnTopCardUser(browser)
        navbar = UpperNavbar(browser)
        navbar.click_user_settings_icon.click()
        navbar.check_invisible_mode().click()
        self.assertion.text_exist(browser, user_card.text_turn_down_invisible)


@suite.register
class CheckInvisibleModeFromMainPage(WebOkSuite):
    @seismograph.step(3, 'Check invisible from main page')
    def check_text(self, browser):
        user_card = LeftColumnTopCardUser(browser)
        user_card.wait_for_invisible_toggler()
        browser.execute_script(user_card.check_invisible_mode)
        user_card.wait_for_invisible_toggler()
        browser.refresh()
        self.assertion.text_exist(browser, user_card.text_turn_down_invisible)


@suite.register
class CheckInvisibleModeFromMobileVersion(selenium.Case):
    @seismograph.step(1, 'Login to m.ok.ru and setup invisible mode')
    def go_to_ok_registered(self, browser):
        morda = OkMobileMorda(browser)
        browser.go_to(morda.link)
        morda.email_input.send_keys(AuthManager.get_login())
        morda.password_input.send_keys(AuthManager.get_password())
        morda.submit_btn.first().click()

        user_card = LeftColumnTopCardUserMobile(browser)
        user_card.wait_for_invisible_toggler()
        if user_card.invisible_toggler.first().is_selected():
            browser.execute_script(user_card.invisible_mode)
            browser.refresh()

    @seismograph.step(2, 'Check invisible mode for mobile version')
    def check_text(self, browser):
        user_card = LeftColumnTopCardUserMobile(browser)
        browser.execute_script(user_card.invisible_mode)
        user_card.wait_for_invisible_toggler()
        browser.refresh()
        assert user_card.invisible_toggler.first().is_selected()
