# -*- coding: utf-8 -*-

from selenium.webdriver.support.ui import WebDriverWait
from test_base import Page
from test_base import Component
from seismograph.ext import selenium
from base_case import BaseCase


class GroupSettingsPage(Page):
    PATH = "/group/53389738115166/settings"

    @property
    def main_settings(self):
        return MainSettings(self.driver)

    def refresh_page(self):
        self.driver.refresh()


class GroupPage(Page):
    PATH = "/group/53389738115166"

    def refresh_page(self):
        self.driver.refresh()


class MainSettings(Component):
    NAME_INPUT = "//input[@name='st.name']"
    SAVE = "//input[@name='button_save_settings'][@class='button-pro form-actions_yes h-mod']"
    SAVE_MESSAGE = "//div[@class='tip __active __l __mid __fixed h-mod']"
    DESCRIPTION = "//textarea[@name='st.description']"
    CITY = "//input[@name='st.city']"
    StPetersburg = "//div[@title='Санкт-Петербург, Россия'][@class='sug_it-div']"
    Moscow = "//div[@title='Москва, Россия'][@class='sug_it-div']"

    def get_group_name(self):
        return self.driver.find_element_by_xpath(self.NAME_INPUT).get_attribute('value')

    def change_group_name(self, new_name):
        self.driver.find_element_by_xpath(self.NAME_INPUT).clear()
        self.driver.find_element_by_xpath(self.NAME_INPUT).send_keys(new_name)

    def get_description(self):
        return self.driver.find_element_by_xpath(self.DESCRIPTION).get_attribute('value')

    def change_description(self, new_description):
        self.driver.find_element_by_xpath(self.DESCRIPTION).clear()
        self.driver.find_element_by_xpath(self.DESCRIPTION).send_keys(new_description)

    def get_city(self):
        return self.driver.find_element_by_xpath(self.CITY).get_attribute('value')

    def change_city(self, new_city):

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element_by_xpath(self.CITY).clear()
        self.driver.find_element_by_xpath(self.CITY).send_keys(new_city)

        if new_city == u"Санкт ":
            WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_xpath(self.StPetersburg)
            )
            self.driver.find_element_by_xpath(self.StPetersburg).click()
        else:
            WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_xpath(self.Moscow)
            )
            self.driver.find_element_by_xpath(self.Moscow).click()

    def save_changes(self):
        self.driver.find_element_by_xpath(self.SAVE).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SAVE_MESSAGE)
        )


suite = selenium.Suite(__name__, require=['selenium'])


@suite.register
class GroupsSettingsTest(BaseCase):
    def test_rename_group(self):
        self.group_settings_page = GroupSettingsPage(self.driver)
        self.group_settings_page.open()
        self.main_settings = self.group_settings_page.main_settings

        new_name = u"КОТИКИ"
        last_name = self.main_settings.get_group_name()

        self.main_settings.change_group_name(new_name)
        self.main_settings.save_changes()
        self.assertion.equal(new_name, self.main_settings.get_group_name())

        self.main_settings.change_group_name(last_name)
        self.main_settings.save_changes()
        self.assertion.equal(last_name, self.main_settings.get_group_name())

    def test_change_description(self):
        new_description = u"Мое описание самое лучшее, самое важное, никем не загаженное"
        self.group_settings_page = GroupSettingsPage(self.driver)
        self.group_settings_page.open()
        self.main_settings = self.group_settings_page.main_settings
        last_description = self.main_settings.get_description()

        self.main_settings.change_description(new_description)
        self.main_settings.save_changes()
        self.assertion.equal(new_description, self.main_settings.get_description())

        self.main_settings.change_description(last_description)
        self.main_settings.save_changes()
        self.assertion.equal(last_description, self.main_settings.get_description())

    def test_change_city(self):
        self.group_settings_page = GroupSettingsPage(self.driver)
        self.group_settings_page.open()
        self.main_settings = self.group_settings_page.main_settings
        new_city = u"Санкт "
        right_new_city = u"Санкт-Петербург"
        last_city = self.main_settings.get_city()

        self.main_settings.change_city(new_city)

        self.main_settings.save_changes()
        self.assertion.equal(right_new_city, self.main_settings.get_city())

        self.main_settings.change_city(last_city)
        self.main_settings.save_changes()
        self.assertion.equal(last_city, self.main_settings.get_city())
