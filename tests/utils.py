# -*- coding: utf-8 -*-

import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


# def custom_move_to_element(driver, element_xpath):
#     """Move to element.

#     Note: Current browser versions and selenium version upper 3.0
#           have not resolved bug (`ActionChains` doesn't work especially
#           `move_to_element` method)

#     """
#     wait = WebDriverWait(driver, 10)
#     element = wait.until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
#     element.click()

#     wait = WebDriverWait(driver, 10)
#     element = wait.until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
#     element.click()


# def custom_move_to_element(driver, element_css_selector, element_xpath, click_times=2):
#     """Move to element.

#     Note:
#         Current browser versions and selenium version upper 3.0
#         have not resolved bug (`ActionChains` doesn't work especially
#         `move_to_element` method).

#         It's attempt to find solution from this problem by clicking target element
#         where we supposed to be by moving.

#         `click_times` param is needed for moving to like button. If we just click to this
#         element we break like information. In this situation we should just click twice to
#         restore like information.

#     Args:
#         `element_xpath` and `element_css_selector` - path to to the same element.
#             Passing different selectors cause of
#             ``EC.element_to_be_clickable((By.CSS_SELECTOR, element_css_selector))``
#             gives understandable error.

#     """
#     for i in range(click_times):
#         WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
#             (By.XPATH, element_xpath))
#         )
#         driver.execute_script('$("%s").click()' % element_css_selector)
#     time.sleep(5)

def custom_move_to_element(driver, element_xpath, click_times=2):
    """Move to element.

    Note:
        Current browser versions and selenium version upper 3.0
        have not resolved bug (`ActionChains` doesn't work especially
        `move_to_element` method).

        It's attempt to find solution from this problem by clicking target element
        where we supposed to be by moving.

        `click_times` param is needed for moving to like button. If we just click to this
        element we break like information. In this situation we should just click twice to
        restore like information.

    """
    # print('in custom_move_to_element')
    # for i in range(click_times):
    #     time.sleep(1)
    #     driver.execute_script('$("%s").click()' % element_css_selector)
    # # for popup to be visible
    # time.sleep(5)
    for i in range(click_times):
        time.sleep(1)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, element_xpath))
        ).click()
        # driver.execute_script('$("%s").click()' % element_css_selector)
    time.sleep(5)
