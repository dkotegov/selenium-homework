from seismograph.ext import selenium
#from seismograph.ext.selenium import PageElement as PE
#from seismograph.ext.selenium import query as _
import utils

class NewVideos(selenium.Page):
    __url_path__ = '/video/new'
    FIRST_VIDEO = '(//div[@class="vid-card"])[1]/a'
    first_video_query =  utils.query("DIV", _class='vid-card')

    def open_first_video(self):
        link = self.first_video_query.first().a()
        #link = utils.wait_xpath(self.driver, self.FIRST_VIDEO)
        #href = link.get_attribute('href')
        href = link.attr.href
        link.click()
        utils.wait_change_url(self.browser)
        return href