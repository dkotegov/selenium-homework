# coding=utf-8
from selenium.common.exceptions import WebDriverException


class text_to_be_present_in_element:
    def __init__(self, element, text_):
        self.element = element
        self.text = text_

    def __call__(self, driver):
        try:
            return self.text in self.element.text
        except WebDriverException:
            return False


class in_url:
    def __init__(self, url):
        self.url = url

    def __call__(self, driver):
        try:
            return self.url in driver.current_url
        except WebDriverException:
            return False


class list_len_equals:
    def __init__(self, locator, count):
        self.locator = locator
        self.count = count

    def __call__(self, driver):
        try:
            new_count = len(driver.find_elements(*self.locator))
            return new_count == self.count
        except WebDriverException:
            return False
