# coding=utf-8
from seismograph.ext import selenium

from pages.payment_modal import PaymentModal
from utils.xpath_query import XPathQueryObject
from selenium.webdriver.support.wait import WebDriverWait
from seismograph.ext.selenium.exceptions import PollingTimeoutExceeded
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException


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
            selenium.query.DIV,
            _class='portlet __toolbar-pmnt',
        )
    )

    five_plus_payment_button = selenium.PageElement(
        XPathQueryObject(
            '//li[contains(text(), "st.layer.srv=1&")]'
        )
    )

    smiles_payment_button = selenium.PageElement(
        XPathQueryObject(
            '//li[contains(text(), "st.layer.srv=19&")]'
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

    frame_wrapper = 'modal-new_ctn'

    smiles_payment_button_locator = '.portlet.__toolbar-pmnt .u-menu .u-menu_li:nth-child(8)'

    five_plus_payment_button_locator = '.portlet.__toolbar-pmnt .u-menu .u-menu_li:nth-child(7)'

    five_plus_checkbox_1_locator = '#val_30'

    five_plus_checkbox_2_locator = '#val_-1'

    smiles_cost_wrapper_locator = '.pf_info_tx.pf_price'

    five_plus_cost_wrapper_locator = '.pf_info_tx.pf_price'

    five_plus_cost_locator = 'span[data-name="prPrice"]'

    smiles_cost_locator = 'span[data-name="prPrice"]'

    smiles_checkbox_1_locator = '#val_5'

    smiles_checkbox_2_locator = '#val_30'

    smiles_checkbox_3_locator = '#val_-1'

    paid_functions_locator = '.nav-side .nav-side_i:nth-child(2)'

    paid_functions_smiles_locator = '.pf_order_lst .pf_order_i:nth-child(3)'

    paid_functions_five_plus_locator = '.pf_order_lst .pf_order_i:nth-child(1)'

    def is_payment_iframe_open(self):
        self.payment_iframe.wait(timeout=3)
        return self.payment_iframe.exist

    def open_payment_dropdown(self):
        self.payment_button.click()
        self.payment_dropdown.wait(timeout=3)

    def open_five_plus_payment_from_dropdown(self):
        try:
            self.five_plus_payment_button.wait(timeout=3)
        except PollingTimeoutExceeded:
            WebDriverWait(self.browser, 3).until(
                lambda br: br.find_element_by_css_selector(self.five_plus_payment_button_locator)
            )
        five_plus_payment_button = self.browser.find_element_by_css_selector(self.five_plus_payment_button_locator)
        five_plus_payment_button.click()
        self.payment_iframe.wait(timeout=3)

    def open_smiles_payment_from_dropdown(self):
        try:
            self.smiles_payment_button.wait(timeout=3)
        except PollingTimeoutExceeded:
            WebDriverWait(self.browser, 3).until(
                lambda br: br.find_element_by_css_selector(self.smiles_payment_button_locator)
            )
        smiles_payment_button = self.browser.find_element_by_css_selector(self.smiles_payment_button_locator)
        smiles_payment_button.click()
        self.payment_iframe.wait(timeout=3)

    def open_toolbar_dropdown(self):
        self.toolbar_dropdown_button.click()
        self.toolbar_dropdown.wait(timeout=2)

    def open_payments_from_dropdown(self):
        self.all_payments_button.click()
        self.payment_iframe.wait()

    def switch_to_last_frame(self):
        payment_modal = PaymentModal(self.browser)
        payment_modal.switch_to_iframe()

    def switch_to_main_window(self):
        self.browser.switch_to_default_content()

    def get_five_plus_cost(self):
        self.switch_to_last_frame()
        try:
            WebDriverWait(self.browser, 5).until(
                lambda br: br.find_element_by_css_selector(self.five_plus_cost_wrapper_locator)
            )
            cost = self.browser.find_element_by_css_selector(self.five_plus_cost_wrapper_locator).text.split(' ')[1]
        except (StaleElementReferenceException, TimeoutException):
            cost = self.browser.find_element_by_css_selector(self.five_plus_cost_locator).text
        return cost

    def get_smiles_cost(self):
        self.switch_to_last_frame()
        try:
            WebDriverWait(self.browser, 5).until(
                lambda br: br.find_element_by_css_selector(self.smiles_cost_wrapper_locator)
            )
            cost = self.browser.find_element_by_css_selector(self.smiles_cost_wrapper_locator).text.split(' ')[1]
        except (StaleElementReferenceException, TimeoutException):
            cost = self.browser.find_element_by_css_selector(self.smiles_cost_locator).text
        return cost

    def click_five_plus_checkbox_by_index(self, index, expected_cost):
        locator = ''
        if index == 1:
            locator = self.five_plus_checkbox_1_locator
        elif index == 2:
            locator = self.five_plus_checkbox_2_locator
        self.browser.find_element_by_css_selector(locator).click()
        self.switch_to_last_frame()
        try:
            WebDriverWait(self.browser, 3).until(
                lambda br: br.find_element_by_css_selector(self.five_plus_cost_locator).text == expected_cost
            )
        except TimeoutException:
            pass  # Цены на разные типы покупки могут быть одинаковые

    def click_smiles_checkbox_by_index(self, index, expected_cost):
        locator = ''
        if index == 1:
            locator = self.smiles_checkbox_1_locator
        elif index == 2:
            locator = self.smiles_checkbox_2_locator
        elif index == 3:
            locator = self.smiles_checkbox_3_locator
        self.browser.find_element_by_css_selector(locator).click()
        self.switch_to_last_frame()
        try:
            WebDriverWait(self.browser, 3).until(
                lambda br: br.find_element_by_css_selector(self.five_plus_cost_locator).text == expected_cost
            )
        except TimeoutException:
            pass  # Цены на разные типы покупки могут быть одинаковые

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
