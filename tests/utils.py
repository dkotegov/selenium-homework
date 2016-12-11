# -*- coding: utf-8 -*-

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def custom_move_to_element(driver, element_xpath):
    """Move to element.

    Note: Current browser versions and selenium version upper 3.0
          have not resolved bug (`ActionChains` doesn't work especially
          `move_to_element` method)

    """
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
    element.click()

    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
    element.click()
