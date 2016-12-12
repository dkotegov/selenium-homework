from seismograph.ext import selenium

from pages.main_page import MainPage


class AuthPage(selenium.Page):
    __url_path__ = '/'

    email_field = selenium.PageElement(selenium.query(selenium.query.INPUT, _id="field_email"), )

    password_field = selenium.PageElement(selenium.query(selenium.query.INPUT, _id="field_password"), )

    submit_button = selenium.PageElement(
        selenium.query(selenium.query.INPUT, type="submit", _class="button-pro form-actions_yes"),
    )

    def log_in(self, email, password):
        self.email_field.set(email)
        self.password_field.set(password)
        self.submit_button.click()
        main_page = MainPage(self.browser)
        main_page.nav_menu.wait()
