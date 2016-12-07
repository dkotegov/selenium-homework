# coding=utf-8

from seismograph.ext import selenium

from utils.xpath_query import XPathQueryObject


class Page(selenium.Page):
    pass


class AuthPage(Page):
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
            value='Log in',
        )
    )

    def auth(self, login, password):
        self.email_field.set(login)
        self.password_field.set(password)
        self.submit_button.click()
        self.wait_for_auth()

    def wait_for_auth(self):
        profile_page = ProfilePage(self.browser)
        profile_page.avatar.wait()


class ProfilePage(Page):
    __url_path__ = '/'

    avatar = selenium.PageElement(
        selenium.query(
            selenium.query.ANY,
            id='viewImageLinkId'
        )
    )

    buy_link = selenium.PageElement(
        XPathQueryObject(
            '//a/span[contains(text(), "Buy OKs")]'
        )
    )
