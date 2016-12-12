# -*- coding: utf-8 -*-
"""Page element classes."""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

from page_elements import PageElement, LikesController, LikeButton, UnlikeButton, \
    LikedUsersListPopup


class OpenDiscussionLinksChain(PageElement):

    OPEN_ALL_DISCUSSIONS = '//li[contains(@class, "toolbar_nav_i")][2]'
    OPEN_MY_DISCUSSIONS = '//div[@id="d-f-tab-fM"]'
    OPEN_DISCUSSION = '//div[contains(@id, "d-item-MOVIE-")][1]'

    def open(self):
        discussions_list = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.OPEN_ALL_DISCUSSIONS))
        )
        discussions_list.click()

        my_discussions_list = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.OPEN_MY_DISCUSSIONS))
        )
        my_discussions_list.click()

        discussion_chat = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.OPEN_DISCUSSION))
        )
        discussion_chat.click()


class LikeCommentInDisscussion(LikeButton):

    BUTTON_WRAPPER = '(//div[contains(@id, "d-id-cmnt-")])[last()]'
    BUTTON = 'ul.controls-list:last span:eq(1)'

    def like(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.BUTTON_WRAPPER))
        )
        self.driver.execute_script('$("%s").click()' % self.BUTTON)


class UnlikeCommentInDisscussion(UnlikeButton):

    BUTTON_WRAPPER = '(//div[contains(@id, "d-id-cmnt-")])[last()]'
    BUTTON = 'ul.controls-list:last span:eq(1)'

    def unlike(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.BUTTON_WRAPPER))
        )
        self.driver.execute_script('$("%s").click()' % self.BUTTON)


class DiscussionCommentLikesController(LikesController):
    """If you liked item you will get `Вы` else `Класс`

    """
    BUTTON_WRAPPER = '(//div[contains(@id, "d-id-cmnt-")])[last()]'
    BUTTON = 'ul.controls-list:last span:eq(1)'

    def has_your_like(self, ):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.BUTTON_WRAPPER))
        )
        like_label = self.driver.execute_script(
            'return $("%s")[0].textContent' % self.BUTTON
        )
        return like_label == u'Вы'


class DiscussionCommentLikedUsers(LikedUsersListPopup):

    LINK = '//a[contains(@class, "al controls-list_counter")]'
    USERNAME_LINK = '(//div[@class="userCard"])[1]/descendant::a[2]'
    CLOSE = '//input[@name="button_close"]'

    def has_your_like(self, username):
        username = unicode(username, 'utf8')
        users_list = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.LINK))
        )
        users_list.click()

        first_username = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.USERNAME_LINK))
        )
        return first_username.text == username

    def close_popup(self):
        close_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.CLOSE))
        )
        close_button.click()


class LikeLikedByOtherUsersCommentInDisscussion(LikeCommentInDisscussion):

    BUTTON_WRAPPER = '(//div[contains(@id, "d-id-cmnt-")])[1]'
    BUTTON = 'ul.controls-list:first span:eq(1)'


class UnlikeLikedByOtherUsersCommentInDisscussion(UnlikeCommentInDisscussion):

    BUTTON_WRAPPER = '(//div[contains(@id, "d-id-cmnt-")])[1]'
    BUTTON = 'ul.controls-list:first span:eq(1)'
