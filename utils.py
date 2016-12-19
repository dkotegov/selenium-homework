# -*- coding: utf-8 -*-
from seismograph.ext import selenium
from selenium.common.exceptions import StaleElementReferenceException




def raises_stale_element_reference_exception(func, *args, **kwargs):
    try:
        func(*args, **kwargs)
        return True
    except StaleElementReferenceException:
        return False


def repeat_on_error(func):
    def wrapper(*args, **kwargs):
        return args[0].browser.waiting_for(
            lambda: raises_stale_element_reference_exception(func, *args, **kwargs)
        )

    return wrapper


def wait_xpath(driver, xpath, timeout=None):
    return driver.waiting_for(lambda : driver.find_element_by_xpath(xpath), timeout)


def wait_many_xpath(driver, xpath, timeout=None):
    return driver.waiting_for(lambda: driver.find_elements_by_xpath(xpath), timeout)


def wait_id(driver, id, timeout=None):
    return driver.waiting_for(lambda: driver.find_element_by_id(id), timeout)


def wait_name(driver, name, timeout=None):
    return driver.waiting_for(lambda: driver.find_element_by_name(name), timeout)


def wait_many_class(driver, cls, timeout=None):
    return driver.waiting_for(lambda: driver.find_elements_by_class_name(cls), timeout)


def wait_class(driver, cls, timeout=None):
    return driver.waiting_for(lambda: driver.find_element_by_class_name(cls), timeout)


def wait_change_url(driver, timeout=None):
    current_url = driver.current_url
    return driver.waiting_for(lambda: driver.current_url != current_url, timeout)


def wait_value(driver, xpath, value, timeout=None):
    return driver.waiting_for(lambda: driver.find_element_by_xpath(xpath).text == value, timeout)


def wait_screen_change(driver, xpath, timeout=None):
    size = driver.find_element_by_xpath(xpath).size['width']
    return driver.waiting_for(lambda: driver.find_element_by_xpath(xpath).size['width'] != size, timeout)


def replace_text(web_element, new_text):
    web_element.clear()
    web_element.send_keys(new_text)

def set_attribute(driver, element, attribute, value):
    driver.execute_script(
        'arguments[0].{}="{}";'.format(attribute, value),
        element._wrapped
    )

def js_click(driver, element):
    driver.execute_script('arguments[0].click();', element._wrapped)


def js_set_text(driver, element, text):
    driver.execute_script('arguments[0].innerHTML = arguments[1];', element._wrapped, text)


def js_value(driver, element):
    return driver.execute_script('return arguments[0].innerHTML;', element._wrapped)


def query(tag, **kwargs):
    pe_params = {}

    if 'pe_property' in kwargs:
        pe_params['property'] = kwargs['pe_property']
        del kwargs['pe_property']
    if 'pe_call' in kwargs:
        pe_params['call'] = kwargs['pe_call']
        del kwargs['pe_call']

    return selenium.PageElement(
        selenium.query(
            getattr(selenium.query, tag),
            **kwargs
        ), **pe_params
    )


def text_field(tag, **kwargs):
    kwargs.update({'pe_property': lambda we: we.text})
    return query(tag, **kwargs)


def time_to_int(time):
    time = time.split(':')
    result = 0
    if len(time) == 3:
        result = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
    if len(time) == 2:
        result = int(time[0]) * 60 + int(time[1])
    if len(time) == 1:
        result = int(time[0] or 0)

    return result


def int_to_time(x):
    result = ''
    hours = 0
    if x >= 3600:
        hours = x / 3600
        result += str(hours) + ':'

    minutes = x / 60 - hours * 60
    if x >= 3600 and minutes < 10:
        result += '0'
    result += str(minutes) + ':'

    seconds = x - minutes * 60 - hours * 3600
    if seconds < 10:
        result += '0'
    result += str(seconds)
    return result
