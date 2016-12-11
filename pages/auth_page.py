from .base import Component, Page


class AuthPage(Page):
    PATH = ''
    TITLE = 'OK.RU'

    @property
    def form(self):
        return AuthForm(self.driver)


class AuthForm(Component):
    LOGIN_XPATH = '//input[@name="st.email"]'
    PASSWORD_XPATH = '//input[@name="st.password"]'
    SUBMIT_XPATH = '//*[@class="button-pro form-actions_yes"]'  # TODO

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN_XPATH).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD_XPATH).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT_XPATH).click()

    def signin(self, login, password):
        self.set_login(login)
        self.set_password(password)
        self.submit()
