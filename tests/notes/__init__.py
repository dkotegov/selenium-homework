# -*- coding: utf-8 -*-

from conf.base import OK_URL

from seismograph.ext import selenium
from selenium.common.exceptions import NoSuchElementException

from utils.forms import AuthForm
from utils.pages import BasePage

"""pizdec
__all__ = [
    'AuthSuite'
]


class AuthSuite(selenium.Suite):

    def setup(self, *args, **kwargs):
        with self.ext('selenium') as browser:
            browser.go_to(OK_URL)

            auth_form = AuthForm(browser)
            auth_form.fill()
            auth_form.submit()


    def teardown(self, *args, **kwargs):

        with self.ext('selenium') as browser:
            browser.go_to(OK_URL)

            page = BasePage(browser)
            # Проверяем, не остались ли мы авторизованы после закрытия браузера
            try:
                page.exit_link.click()
            except NoSuchElementException:
                pass

"""
