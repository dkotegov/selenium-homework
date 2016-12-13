# -*- coding: utf-8 -*-
"""Page element classes."""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

from utils import custom_move_to_element


class PageElement(object):

    def __init__(self, driver):
        self.driver = driver


class AuthForm(PageElement):

    LOGIN = '//input[@name="st.email"]'
    PASSWORD = '//input[@name="st.password"]'
    SUBMIT = '//input[@class="button-pro form-actions_yes"]'
    LOGGED_USERNAME = '//h1[contains(@class, "mctc_name_tx")]'

    def set_username(self, username):
        self.username = username

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(password)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    @property
    def is_logged(self):
        try:
            WebDriverWait(self.driver, 10, 0.1).until(
                EC.text_to_be_present_in_element(
                    (By.XPATH, self.LOGGED_USERNAME), self.username
                )
            )
            return True
        except TimeoutException:
            return False


class LikesController(PageElement):
    """The page element to show visually your like or not if you didn't like it.

    """
    def has_your_like(self):
        pass


class LikedUsersListPopup(PageElement):
    """The page element to show users who liked item.

    """
    LINK_XPATH = '//div[contains(@class, "photo-layer_bottom_block __actions")]//descendant::li[last()]/descendant::button'
    USERNAME_LINK = '(//ul[@class="ucard-mini-list"]/li/descendant::div[@class="ucard-mini_cnt_i ellip"])[1]'

    def has_your_like(self, username):
        """Check presence your `username` in liked users.

        Note:
            Your login must be on the top in list of users if you liked it.
            In the other case your login shouldn't be there.

        """
        username = unicode(username, 'utf8')
        custom_move_to_element(
            self.driver, self.LINK_XPATH, click_times=2
        )

        first_user = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.USERNAME_LINK))
        )
        return first_user.text == username


class LikeButton(PageElement):
    """The page element to like item.

    """
    BUTTON = ''

    def like(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, self.BUTTON))
        ).click()


class UnlikeButton(PageElement):
    """The page element to unlike item.

    """
    BUTTON = ''

    def unlike(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, self.BUTTON))
        ).click()
