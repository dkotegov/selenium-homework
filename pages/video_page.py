from base import Page, Component
import utils


class VideoPage(Page):
    VIDEO_TITLE_XPATH = '//div[@class="portlet_h portlet_h__nb textWrap"]'
    VIDEO_DESCRIPTION_XPATH = '//div[@class="media-text_cnt textWrap js-vp-layer-description_tx"]'
    CLOSE_VIDEO = '//div[@class="ic media-layer_close_ico"]'

    def __init__(self, driver, path):
        super(VideoPage, self).__init__(driver)
        self.PATH = path

    @property
    def description(self):
        return utils.wait_xpath(self.driver, self.VIDEO_DESCRIPTION_XPATH).text

    @property
    def title(self):
        return utils.wait_xpath(self.driver, self.VIDEO_TITLE_XPATH).text

    def close_video(self):
        utils.wait_xpath(self.driver, self.CLOSE_VIDEO).click()
