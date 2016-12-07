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

    five_plus_checkbox_1_locator = 'label[for="val_30"]'

    five_plus_checkbox_2_locator = 'label[for="val_-1"]'

    five_plus_cost_locator = 'span[data-name="prPrice"]'


    def is_five_plus_payment_open(self):
        self.five_plus_iframe.wait(timeout=3)
        return self.five_plus_iframe.exist

    def open_payment_dropdown(self):
        self.payment_button.click()
        self.payment_dropdown.wait(timeout=3)

    def open_five_plus_payment_from_dropdown(self):
        time.sleep(2)  # Wait for eventListeners
        self.five_plus_payment_button.click()
        self.five_plus_iframe.wait()

    def switch_to_last_frame(self):
        time.sleep(3)  # time for iframe to load data
        frames = self.browser.find_elements_by_css_selector('iframe')
        self.browser.switch_to.frame(len(frames) - 1)

    def switch_to_main_window(self):
        self.browser.switch_to_default_content()

    def get_five_plus_cost(self):
        return self.browser.find_element_by_css_selector(self.five_plus_cost_locator).get_attribute('innerHTML')

    def click_checkbox_by_index(self, index):
        locator = ''
        if index == 1:
            locator = self.five_plus_checkbox_1_locator
        elif index == 2:
            locator = self.five_plus_checkbox_2_locator
        self.browser.find_element_by_css_selector(locator).click()
        time.sleep(5)  # Time for iframe to load data







