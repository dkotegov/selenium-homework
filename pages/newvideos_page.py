from .base import Page, Component
import utils


class NewVideos(Page):
    PATH = 'video/new'
    FIRST_VIDEO = '(//div[@class="vid-card"])[1]'

    def open_first_video(self):
        utils.wait_xpath(self.driver, self.FIRST_VIDEO).click()
        utils.wait_change_url(self.driver)
