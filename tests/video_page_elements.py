# -*- coding: utf-8 -*-
"""Page element classes."""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from page_elements import LikesController, LikeButton, UnlikeButton, \
    LikedUsersListPopup, PageElement


class LikeVideoButtonUnderPlayer(LikeButton):

    BUTTON = '//ul[@class="widget-list"]/descendant::button[last()]'

    HIGHLIGHTED_ELEMENT = '//ul[@class="widget-list"]/descendant::button[last()]/parent::*'

    def like_highlighted(self):
        class_name = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.HIGHLIGHTED_ELEMENT))
        ).get_attribute('class')
        return 'active' in class_name


class UnlikeVideoButtonUnderPlayer(UnlikeButton):

    BUTTON = '//ul[@class="widget-list"]/descendant::button[last()]'


class LikeVideoButtonInsidePlayer(LikeButton):

    BUTTON = 'html5-vpl_ac_i'

    def like(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.BUTTON))
        )
        self.driver.execute_script('$(".%s")[0].click()' % self.BUTTON)


class UnlikeVideoButtonInsidePlayer(LikeButton):

    BUTTON = 'html5-vpl_ac_i'

    def unlike(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.BUTTON))
        )
        self.driver.execute_script('$(".%s")[0].click()' % self.BUTTON)


class ButtonInsidePlayerLikesController(LikesController):

    LINK = 'html5-vpl_ac_txt'

    def has_your_like(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.LINK))
        )
        message = self.driver.execute_script('return $(".html5-vpl_ac_txt")[0].textContent')
        return u'Вы' in message


class VideoLikedUsers(LikedUsersListPopup):

    LINK_XPATH = '//ul[@class="widget-list"]/descendant::button[last()]'
    USERNAME_LINK = '//ul[@class="ucard-mini-list"]/li/descendant::div[@class="ucard-mini_cnt_i ellip"]'


class CloseVideoButton(PageElement):

    BUTTON = '(//div[@class="ic media-layer_close_ico"])[1]'

    def click(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.BUTTON))
        ).click()
