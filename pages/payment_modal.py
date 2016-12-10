# coding=utf-8
import time
from seismograph.ext import selenium
from seismograph.ext.selenium.query import Contains

from utils.xpath_query import XPathQueryObject


class PaymentModal(selenium.Page):
    buy_link = selenium.PageElement(
        XPathQueryObject(
            u'//a/span[contains(text(), "Купить ОКи")]'
        )
    )

    modal_close_button = selenium.PageElement(
        selenium.query(
            selenium.query.A,
            _id='nohook_modal_close'
        )
    )

    iframe = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _id='pmntWzrdCtr',
        )
    )

    def open(self):
        self.browser.execute_script('document.getElementById("topPanel").style.visibility="hidden"')
        self.buy_link.click()

    def close(self):
        self.modal_close_button.click()

    def is_open(self):
        return self.iframe.is_displayed()

    def switch_to_iframe(self, sel='*'):
        self.browser.switch_to.default_content()
        frames = self.browser.find_elements_by_css_selector('iframe')
        self.iframe.wait(10)

        max_els = 0
        max_els_frame = 1
        for i in range(0, len(frames)):
            try:
                self.browser.switch_to.frame(i)
            except:
                continue
            els = self.browser.find_element_by_css_selector('body').find_elements_by_css_selector(sel)

            if len(els) > max_els:
                max_els = len(els)
                max_els_frame = i
            self.browser.switch_to.default_content()

        self.browser.switch_to.frame(max_els_frame)

    def open_tab(self, index):
        def get_tab_links():
            self.switch_to_iframe()
            return self.browser.find_elements_by_css_selector('a.nav-side_i')

        tab_links = []

        tries = 0
        while tries < 5 and index >= len(tab_links):
            tab_links = get_tab_links()
            tries += 1

        tab_links[index].click()
        self.browser.switch_to.default_content()

    def open_tab_transactions(self):
        self.open_tab(0)

    def get_tab_transaction(self):
        self.switch_to_iframe()
        return self.browser.div(_class=Contains('pf_layout'))

    def open_tab_my_services(self):
        self.open_tab(1)

    def get_tab_my_services_els(self):
        self.switch_to_iframe()
        return self.browser.div(_class=Contains('pf_order_i'))

    def open_tab_my_cards(self):
        self.open_tab(2)

    def get_tab_my_cards_add(self):
        self.switch_to_iframe()
        return self.browser.div(_class=Contains('add-stub_tx'))

    def get_tab_my_cards_add_link(self):
        self.switch_to_iframe()
        return self.browser.a(_class=Contains('add-stub__hor'))

    def open_tab_bank_card(self):
        self.open_tab(3)

    def get_tab_bank_card_input(self):
        self.switch_to_iframe()
        return self.browser.input('#cardnumber')

    def open_tab_phone(self):
        self.open_tab(4)

    def get_tab_phone_input(self):
        self.switch_to_iframe()
        return self.browser.input(_id='phoneInput')

    def get_tab_phone_select(self):
        self.browser.switch_to.default_content()
        self.switch_to_iframe()
        return self.browser.select(_id='ctrSelect')

    def get_tab_phone_els(self):
        self.browser.switch_to.default_content()
        self.switch_to_iframe()
        return self.browser.label(_class=Contains('pf_phone_i'))

    def open_tab_terminal(self):
        self.open_tab(5)

    def get_tab_terminal_select(self):
        self.switch_to_iframe()
        return self.browser.select(_id='ctrSelect')

    def get_tab_terminal_els(self):
        self.browser.switch_to.default_content()
        self.switch_to_iframe()
        return self.browser.a(_class=Contains('pf_external-refill_i'))

    def open_tab_emoney(self):
        self.open_tab(6)

    def get_tab_emoney_els(self):
        self.switch_to_iframe()
        return self.browser.a(_class=Contains('pf_external-refill_i'))
