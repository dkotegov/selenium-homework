from seismograph.ext import selenium


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
            value='Log in',
        )
    )

    def auth(self, login, password):
        self.email_field.set(login)
        self.password_field.set(password)
        self.submit_button.click()
