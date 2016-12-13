# -*- coding: utf-8 -*-

import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


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
    for i in range(click_times):
        time.sleep(1)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, element_xpath))
        ).click()
    time.sleep(5)
