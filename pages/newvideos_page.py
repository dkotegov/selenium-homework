from .base import Page, Component
import utils


class NewVideos(Page):
    PATH = 'video/new'
    FIRST_VIDEO = '(//div[@class="vid-card"])[1]/a'

    def open_first_video(self):
        link = utils.wait_xpath(self.driver, self.FIRST_VIDEO)
        href = link.get_attribute('href')
        link.click()
        utils.wait_change_url(self.driver)
        return href

