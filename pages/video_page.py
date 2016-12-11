from seismograph.ext import selenium
from smth.xpath import XPathQueryObject

import time

class VideoPage(selenium.Page):
    __url_path__ = '/video/196391273929'


    def repostVideo(self):
        time.sleep(2)
        self.browser.execute_script('''$(':button[tsid=reshareMenu]').last().click()''')
        time.sleep(3)
        self.browser.execute_script('''$("div[data-l*='t,now']").last().find('a').click()''')
        time.sleep(2)
        val = self.browser.find_elements_by_css_selector("span.tico")[31].text
        return val
