# -*- coding: utf-8 -*-

from seismograph.ext import selenium
from pages.feed_page import FeedPage


class AuthPage(selenium.Page):
    __url_path__ = '/dk?st.cmd=anonymMain'

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
            value=u'Войти',
            _class='button-pro form-actions_yes'
        )
    )

    def auth(self, login, password):
        self.email_field.set(login)
        self.password_field.set(password)
        self.submit_button.click()
        self.wait_for_auth()

    def wait_for_auth(self):
        profile_page = FeedPage(self.browser)
        profile_page.right_div.wait()
