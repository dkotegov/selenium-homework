# from .base import Component, Page
from seismograph.ext import selenium
from seismograph.ext.selenium import PageElement as PE
from seismograph.ext.selenium import query as _


class AuthPage(selenium.Page):
    TITLE = 'OK.RU'
    __url_path__ = '/'


    login_field = PE(_(_.INPUT, name="st.email"))
    password_field = PE(_(_.INPUT, name="st.password"))
    submit_button = PE( _(_.INPUT, _class = "button-pro form-actions_yes") )

    def signin(self, login, password):
        self.login_field.set(login)
        self.password_field.set(password)
        self.submit_button.click()