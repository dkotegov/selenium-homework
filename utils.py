# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


DEFAULT_TIMEOUT = 30
DEFAULT_SLEEP_TIME = 0.1

def wait(driver, condition, timeout = DEFAULT_TIMEOUT, sleeptime = DEFAULT_SLEEP_TIME):
    return WebDriverWait(driver, timeout, sleeptime).until(condition)

def wait_xpath(driver, xpath, timeout = DEFAULT_TIMEOUT, sleeptime = DEFAULT_SLEEP_TIME):
    return wait(driver, lambda d: d.find_element_by_xpath(xpath), timeout, sleeptime)

def wait_many_xpath(driver, xpath, timeout = DEFAULT_TIMEOUT, sleeptime = DEFAULT_SLEEP_TIME):
    return wait(driver, lambda d: d.find_elements_by_xpath(xpath), timeout, sleeptime)

def wait_id(driver, id, timeout = DEFAULT_TIMEOUT, sleeptime = DEFAULT_SLEEP_TIME):
    return wait(driver, lambda d: d.find_element_by_id(id), timeout, sleeptime)

def wait_name(driver, name, timeout = DEFAULT_TIMEOUT, sleeptime = DEFAULT_SLEEP_TIME):
    return wait(driver, lambda d: d.find_element_by_name(name), timeout, sleeptime)

def wait_class(driver, cls, timeout = DEFAULT_TIMEOUT, sleeptime = DEFAULT_SLEEP_TIME):
    return wait(driver, lambda d: d.find_element_by_class_name(cls), timeout, sleeptime)

def wait_change_url(driver, timeout = DEFAULT_TIMEOUT, sleeptime = DEFAULT_SLEEP_TIME):
    current_url = driver.current_url
    return wait(driver, lambda d: d.current_url != current_url, timeout, sleeptime)

def replace_text(web_element, new_text):
    web_element.clear()
    web_element.send_keys(new_text)