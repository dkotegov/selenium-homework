from seismograph.ext import selenium
from utils.xpath_query import XPathQueryObject

import time


class FeedPage(selenium.Page):
    __url_path__ = '/feed'

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

    five_plus_iframe = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _id='pmntWzrdCtr',
        )
    )

    payment_button = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _id='pmnt_toolbar_button',
        )
    )

    payment_dropdown = selenium.PageElement(
        selenium.query(
            selenium.query.UL,
            _class='u-menu',
        )
    )

    five_plus_payment_button = selenium.PageElement(
        selenium.query(
            selenium.query.A,
            hrefattrs=selenium.query.contains('st.layer.srv=1&'),
        )
    )

    def is_five_plus_payment_open(self):
        self.five_plus_iframe.wait(timeout=3)
        return self.five_plus_iframe.exist

    def open_payment_dropdown(self):
        self.payment_button.click()
        self.payment_dropdown.wait(timeout=3)

    def open_five_plus_payment_from_dropdown(self):
        time.sleep(2)  # Wait for eventListeners
        self.five_plus_payment_button.click()

