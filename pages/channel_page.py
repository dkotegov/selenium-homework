# -*- coding: utf-8 -*-
from .base import Page, Component
from urlparse import urlsplit
from selenium.webdriver.common.keys import Keys

import utils

class ChannelPage(Page):
    DELETE_BUTTON_CLASS = 'vl_ic_delete'
    CHANNEL_NAME_CLASS = 'mml_ucard_n_g'
    EDIT_BUTTON_CLASS = 'vl_ic_edit'
    CONFIRM_DELETE_XPATH ='//input[@value="Удалить"]'

    def __init__(self, driver, path):
        super(ChannelPage, self).__init__(driver)
        self.PATH = path

    def delete_channel(self):
        utils.wait_class(self.driver, self.DELETE_BUTTON_CLASS).click()
        confirm_delete =  utils.wait_xpath(self.driver,self.CONFIRM_DELETE_XPATH)
        confirm_delete.click()
        utils.wait_change_url(self.driver)

    def channel_name(self):
        name_elem = self.driver.find_element_by_class_name(self.CHANNEL_NAME_CLASS)
        return name_elem.text

    def click_edit(self):
        utils.wait_class(self.driver, self.EDIT_BUTTON_CLASS).click()
        return ChangeChannelDialog(self.driver)

    def edit_channel(self, new_name):
        old_name = self.channel_name()
        change_channel_dialog = self.click_edit()
        change_channel_dialog.set_channel_name(new_name)
        page = change_channel_dialog.submit()
        self.wait_change(old_name)
        return page


    def wait_change(self, old_name):
        utils.wait(self.driver, lambda d: self.channel_name() != old_name)


class ChangeChannelDialog(Component):
    CHANNEL_NAME_XPATH = '//input[@name="st.vv_albumName"]'
    CHANNEL_SUBMIT_XPATH = '//input[@value="Сохранить"]'

    def set_channel_name(self, name):
        name_elem = utils.wait_xpath(self.driver, self.CHANNEL_NAME_XPATH)
        #name_elem.clear()
        name_elem.send_keys(Keys.BACKSPACE * 100)#TODO найти решение получше
        name_elem.send_keys(name)

    def submit(self):
        utils.wait_xpath(self.driver, self.CHANNEL_SUBMIT_XPATH).click()
        path = urlsplit(self.driver.current_url).path
        page = ChannelPage(self.driver, path)
        return page