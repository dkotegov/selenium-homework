# -*- coding: utf-8 -*-

import seismograph
from conf.base import OK_URL
from selenium.common.exceptions import NoSuchElementException
from utils.forms import AuthForm
from utils.pages import BasePage


__all__ = [
    'program'
]


class SeleniumProgram(seismograph.Program):

    def setup(self):
        with self.ext('selenium') as browser:
            browser.go_to(OK_URL)

            auth_form = AuthForm(browser)
            auth_form.fill()
            auth_form.submit()

    def teardown(self):
        with self.ext('selenium') as browser:
            browser.go_to(OK_URL)

            page = BasePage(browser)
            # Проверяем, не остались ли мы авторизованы после закрытия браузера
            try:
                page.exit_link.click()
            except NoSuchElementException:
                pass


program = SeleniumProgram(config_path='conf.base', require=['selenium'])
