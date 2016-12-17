from seismograph.ext import selenium

from utils import query


class AuthPage(selenium.Page):
    TITLE = 'OK.RU'
    __url_path__ = '/'

    login_field = query('INPUT', name="st.email")
    password_field = query('INPUT', name="st.password")
    submit_button = query('INPUT', _class="button-pro form-actions_yes")

    def signin(self, login, password):
        self.login_field.set(login)
        self.password_field.set(password)
        self.submit_button.click()
        self.browser.waiting_for(
            lambda: not self.browser.title.startswith(self.TITLE)
        )

