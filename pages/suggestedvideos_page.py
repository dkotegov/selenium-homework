from .base import Page
import utils


class SuggestedVideos(Page):
    PATH = 'video/suggestedAlbums'
    FIRST_VIDEO = '(//a[@class="vid-card vid-card__m slider_i"])[1]'

    def open_first_video(self):
        link = utils.wait_xpath(self.driver, self.FIRST_VIDEO, 3)
        href = link.get_attribute('href')
        link.click()
        utils.wait_change_url(self.driver)
        return href

