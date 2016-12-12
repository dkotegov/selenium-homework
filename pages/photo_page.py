from seismograph.ext import selenium
from smth.xpath import XPathQueryObject

import time

class PhotoPage(selenium.Page):
    __url_path__ = '/profile/572412246941/pphotos/849451663773'

    avatar = selenium.PageElement(
        selenium.query(
            selenium.query.IMG,
            id='viewImageLinkId'
        )
    )

    def repostPhoto(self):
        time.sleep(2)
        self.browser.execute_script('''$(':button[tsid=reshareMenu]').last().click()''')
        time.sleep(3)
        self.browser.execute_script('''$("div[data-l*='t,now']").last().find('a').click()''')
        time.sleep(4)
        val = self.browser.find_elements_by_css_selector("span.tico")[23].text
        return val
