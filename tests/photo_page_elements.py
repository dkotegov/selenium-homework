# -*- coding: utf-8 -*-
"""Page element classes."""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from page_elements import LikeButton, UnlikeButton, LikedUsersListPopup, \
    LikesController


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


class PhotoLikedUsersInAlbum(PhotoLikedUsers):

    LINK_XPATH = '(//li[contains(@class, "ugrid_i")])[1]//descendant::li[1]'


class LikeButtonAvatarPhoto(LikeButton):

    BUTTON = '(//div[contains(@class, "lcTc_avatar __l")]/descendant::span)[last()]'


class UnlikeButtonAvatarPhoto(UnlikeButton):

    BUTTON = '(//div[contains(@class, "lcTc_avatar __l")]/descendant::span)[last()]'


class ListAvatarPhotoLikedUsers(LikesController):

    BUTTON = '(//div[contains(@class, "lcTc_avatar __l")]/descendant::span)[last()]'

    def has_your_like(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, self.BUTTON))
        )
        return u'Вы'in element.text
