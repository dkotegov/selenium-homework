# coding=utf-8
from seismograph.ext import selenium
from smth.xpath import XPathQueryObject

import time


class ElsePostPage(selenium.Page):
    __url_path__ = '/profile/573666484126/statuses/65858517120414'

    post_text = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            id='posting_form_text_field'
        )
    )

    def makeRepost(self):
        time.sleep(2)
        self.browser.execute_script('''$(':button[tsid=reshareMenu]').last().click()''')
        time.sleep(3)
        self.browser.execute_script('''$("div[data-l*='t,now']").last().find('a').click()''')
        time.sleep(4)
        val = self.browser.find_elements_by_css_selector("span.tico")
        for a in val:
            if a.text == u'Опубликовано!':
                val = a.text
        return val

    def makeLike(self):
        return 1
