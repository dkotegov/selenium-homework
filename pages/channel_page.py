# -*- coding: utf-8 -*-
from .base import Page, Component
from urlparse import urlsplit
from selenium.webdriver.common.keys import Keys

import utils

class ChannelPage(Page):
    DELETE_BUTTON_CLASS = 'vl_ic_delete'
    DELETE_VIDEO_SUBMIT_XPATH = '//input[@value="Удалить"]'
    CHANNEL_NAME_CLASS = 'mml_ucard_n_g'
    EDIT_BUTTON_CLASS = 'vl_ic_edit'
    ADD_VIDEO_CLASS ='vl_ic_add-video'
    CONFIRM_DELETE_XPATH ='//input[@value="Удалить"]'
    VIDEO_XPATH_TEMPLATE = '//div[@class="vid-card js-sortable"]/child::a[@title="{}"]/descedant::span[@class="tico_img vl_ic_delete"]' #TODO Исправить
    DELETE_FIRST_VIDEO_XPATH ='//a[@class="vid-card_ac_i ic vl_ic_delete"]'
    DELETE_FIRST_VIDEO_JS = '''$x('{}')[0].click()'''.format(DELETE_FIRST_VIDEO_XPATH)

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

    def click_add_video(self):
        utils.wait_class(self.driver, self.ADD_VIDEO_CLASS).click()
        return AddVideoDialog(self.driver)

    def add_video_by_url(self, url):
        add_video_dialog = self.click_add_video()
        add_video_dialog.choose_add_from_internet()
        add_video_dialog.set_url(url)
        return add_video_dialog.submit()

    def edit_channel(self, new_name):
        old_name = self.channel_name()
        change_channel_dialog = self.click_edit()
        change_channel_dialog.set_channel_name(new_name)
        page = change_channel_dialog.submit()
        self.wait_change(old_name)
        return page

    def delete_video_by_name(self, name):
        utils.wait_xpath(self.driver, self.VIDEO_XPATH_TEMPLATE.format(name)).click()
        utils.wait_xpath(self.driver, self.DELETE_VIDEO_SUBMIT_XPATH).click()

    def delete_video(self):
        delete_button = utils.wait_xpath(self.driver, self.DELETE_FIRST_VIDEO_XPATH)
        self.driver.execute_script('arguments[0].click();', delete_button)
        utils.wait_xpath(self.driver, self.DELETE_VIDEO_SUBMIT_XPATH).click()

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

class AddVideoDialog(Component):
    FROM_INTERNET_XPATH = '//span[@data-target="video_uploader_link"]'
    VIDEO_URL_XPATH ='//input[@name="st.vv_ugLink"]'
    ADD_VIDEO_XPATH = '//div[@class="form-actions video_uploader_actions"]/child::button[text()="Добавить"]'

    def choose_add_from_internet(self):
        utils.wait_xpath(self.driver, self.FROM_INTERNET_XPATH).click()

    def set_url(self, url):
        utils.wait_xpath(self.driver, self.VIDEO_URL_XPATH).send_keys(url)

    def submit(self):
        utils.wait_xpath(self.driver, self.ADD_VIDEO_XPATH).click()
        path = urlsplit(self.driver.current_url).path
        page = ChannelPage(self.driver, path)
        return page
