# coding=utf-8
from seismograph.ext import selenium

from pages.payment_modal import PaymentModal
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

    payment_iframe = selenium.PageElement(
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

    smiles_payment_button = selenium.PageElement(
        selenium.query(
            selenium.query.A,
            hrefattrs=selenium.query.contains('st.layer.srv=19&'),
        )
    )

    toolbar_dropdown_button = selenium.PageElement(
        XPathQueryObject(
            '//div[@data-module="Toolbar"]'
        )
    )

    toolbar_dropdown = selenium.PageElement(
        XPathQueryObject(
            '//div[@class="toolbar_dropdown"]/ul[@class="u-menu"]'
        )
    )

    all_payments_button = selenium.PageElement(
        selenium.query(
            selenium.query.A,
            _class='u-menu_a tdn',
            hrefattrs=selenium.query.contains('st.layer.srv=22&'),
        )
    )

    five_plus_checkbox_1_locator = 'label[for="val_30"]'

    five_plus_checkbox_2_locator = 'label[for="val_-1"]'

    five_plus_cost_locator = 'span[data-name="prPrice"]'

    smiles_cost_locator = 'span[data-name="prPrice"]'

    smiles_checkbox_1_locator = 'label[for="val_5"]'

    smiles_checkbox_2_locator = 'label[for="val_30"]'

    smiles_checkbox_3_locator = 'label[for="val_-1"]'

    paid_functions_locator = 'a[href*="st.mode=47"]'

    paid_functions_smiles_locator = 'div.va_target a[href*="st.srv=19"]'

    paid_functions_five_plus_locator = 'div.va_target a[href*="st.srv=1&"]'

    def is_payment_iframe_open(self):
        self.payment_iframe.wait(timeout=3)
        return self.payment_iframe.exist

    def open_payment_dropdown(self):
        self.payment_button.click()
        self.payment_dropdown.wait(timeout=3)

    def open_five_plus_payment_from_dropdown(self):
        time.sleep(2)  # Wait for eventListeners
        self.five_plus_payment_button.click()
        self.payment_iframe.wait()

    def open_smiles_payment_from_dropdown(self):
        time.sleep(2)  # Wait for eventListeners
        self.smiles_payment_button.click()
        self.payment_iframe.wait()

    def open_toolbar_dropdown(self):
        self.toolbar_dropdown_button.click()
        self.toolbar_dropdown.wait(timeout=2)

    def open_payments_from_dropdown(self):
        self.all_payments_button.click()
        self.payment_iframe.wait()

    def switch_to_last_frame(self):
        time.sleep(3)  # time for iframe to load data
        frames = self.browser.find_elements_by_css_selector('iframe')
        self.browser.switch_to.frame(len(frames) - 1)

    def switch_to_main_window(self):
        self.browser.switch_to_default_content()

    def get_five_plus_cost(self):
        return self.browser.find_element_by_css_selector(self.five_plus_cost_locator).get_attribute('innerHTML')

    def get_smiles_cost(self):
        return self.browser.find_element_by_css_selector(self.smiles_cost_locator).get_attribute('innerHTML')

    def click_five_plus_checkbox_by_index(self, index):
        locator = ''
        if index == 1:
            locator = self.five_plus_checkbox_1_locator
        elif index == 2:
            locator = self.five_plus_checkbox_2_locator
        self.browser.find_element_by_css_selector(locator).click()
        time.sleep(2)  # Time for iframe to load data

    def click_smiles_checkbox_by_index(self, index):
        locator = ''
        if index == 1:
            locator = self.smiles_checkbox_1_locator
        elif index == 2:
            locator = self.smiles_checkbox_2_locator
        elif index == 3:
            locator = self.smiles_checkbox_3_locator
        self.browser.find_element_by_css_selector(locator).click()
        time.sleep(2)  # Time for iframe to load data

    def click_paid_functions(self):
        self.browser.find_element_by_css_selector(self.paid_functions_locator).click()

    def is_smiles_available_in_paid_functions(self):
        buy_smiles = self.browser.find_element_by_css_selector(self.paid_functions_smiles_locator)
        return buy_smiles is not None

    def is_five_plus_available_in_paid_functions(self):
        buy_five_plus = self.browser.find_element_by_css_selector(self.paid_functions_five_plus_locator)
        return buy_five_plus is not None

    def payment_modal(self):
        return PaymentModal(self.browser)
