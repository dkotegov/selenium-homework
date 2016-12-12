# -*- coding: utf-8 -*-
"""Page element classes."""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

from page_elements import PageElement, LikesController, LikeButton, UnlikeButton, \
    LikedUsersListPopup

from utils import custom_move_to_element


class LikePhotoUnderPhoto(LikeButton):

    BUTTON = '//div[contains(@class, "photo-layer_bottom_block __actions")]//descendant::li[last()]'


class UnlikePhotoUnderPhoto(UnlikeButton):

    BUTTON = '//div[contains(@class, "photo-layer_bottom_block __actions")]//descendant::li[last()]'


class LikePhotoInTheRightPhotoCorner(LikeButton):

    BUTTON = '//span[@class="ico_big-klass-white"]'


class UnlikePhotoInTheRightPhotoCorner(UnlikeButton):

    BUTTON = '//span[@class="ico_big-klass-white"]'


class LikeNotOpenedPhotoInAlbum(LikeButton):

    BUTTON = '(//li[contains(@class, "ugrid_i")])[1]//descendant::li[1]'


class UnlikeNotOpenedPhotoInAlbum(UnlikeButton):

    BUTTON = '(//li[contains(@class, "ugrid_i")])[1]//descendant::li[1]'


class PhotoLikedUsers(LikedUsersListPopup):

    # LINK_CSS_SELECTOR = 'div.photo-layer_bottom_block ul.widget-list > li:last() > div:nth-child(1) button'
    LINK_XPATH = '//div[contains(@class, "photo-layer_bottom_block __actions")]//descendant::li[last()]/descendant::button'
    USERNAME_LINK = '(//ul[@class="ucard-mini-list"]/li/descendant::div[@class="ucard-mini_cnt_i ellip"])[1]'

    def has_your_like(self, username):
        username = unicode(username, 'utf8')
        custom_move_to_element(
            self.driver, self.LINK_XPATH, click_times=2
        )

        first_user = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.USERNAME_LINK))
        )
        return first_user.text == username


class PhotoLikedUsersInAlbum(PhotoLikedUsers):

    LINK_XPATH = '(//li[contains(@class, "ugrid_i")])[1]//descendant::li[1]'
