import utils
from .base import Page
from seismograph.ext import selenium


class SuggestedVideos(selenium.Page):
    __url_path__ = '/video/suggestedAlbums'

    FIRST_VIDEO = '(//a[@class="vid-card vid-card__m slider_i"])[1]'

    def open_first_video(self):
        link = utils.wait_xpath(self.browser, self.FIRST_VIDEO, 3)
        href = link.get_attribute('href')
        link.click()
        utils.wait_change_url(self.browser)
        return href
