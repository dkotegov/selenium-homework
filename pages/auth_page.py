# -*- coding: utf-8 -*-

from seismograph.ext import selenium
from pages.feed_page import FeedPage


class AuthPage(selenium.Page):
    __url_path__ = '/'

    email_field = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            id='field_email',
        )
    )

    password_field = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            id='field_password',
        ),
    )

    submit_button = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            _class='button-pro form-actions_yes'
        )
    )

    def auth(self, login, password):
        self.email_field.set(login)
        self.password_field.set(password)
        self.submit_button.click()
        self.wait_for_auth()

    def wait_for_auth(self):
        feed_page = FeedPage(self.browser)
        feed_page.avatar.wait()

