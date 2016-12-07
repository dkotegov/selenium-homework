# coding=utf-8
from base import Page, Component
import utils

class VideoPage(Page):
    VIDEO_TITLE_XPATH = '//div[@class="portlet_h portlet_h__nb textWrap"]'
    VIDEO_DESCRIPTION_XPATH = '//div[@class="media-text_cnt textWrap js-vp-layer-description_tx"]'
    SUBSCRIBE_XPATH ='//a[text()="Подписаться"]'
    UNSUBSCRIBE_XPATH = '//span[@class="vp-layer_subscribe-lbl ic_quit-lg"]'
    def __init__(self, driver, path):
        super(VideoPage, self).__init__(driver)
        self.PATH = path

    @property
    def description(self):
        return utils.wait_xpath(self.driver, self.VIDEO_DESCRIPTION_XPATH).text

    @property
    def title(self):
        return utils.wait_xpath(self.driver, self.VIDEO_TITLE_XPATH).text

    def subscribe(self):
        utils.wait_xpath(self.driver, self.SUBSCRIBE_XPATH).click()

    def unsubscribe(self):
        unsubscribe_button = utils.wait_xpath(self.driver, self.UNSUBSCRIBE_XPATH)
        self.driver.execute_script('arguments[0].click();', unsubscribe_button)

    def is_subscribe(self):
        #self.open()
        return len(utils.wait_many_xpath(self.driver, self.UNSUBSCRIBE_XPATH)) >0

    def is_not_subscribe(self):
        return len(utils.wait_many_xpath(self.driver, self.SUBSCRIBE_XPATH)) >0
