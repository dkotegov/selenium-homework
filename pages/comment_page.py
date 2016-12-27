from seismograph.ext import selenium
from selenium.common.exceptions import WebDriverException


class CommentPage(selenium.Page):
    comment_body = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            id='topPanelPopup_d'
        )
    )

    comment_input = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            id='ok-e-d'
        )
    )

    @selenium.polling.wrap(timeout=20, delay=1)
    def wait_popup(self):
        if not self.comment_body.is_displayed():
            raise WebDriverException(msg='Timeout at waiting comment modal')
