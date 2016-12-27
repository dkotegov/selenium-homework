# coding=utf-8
from seismograph.ext import selenium
from selenium.common.exceptions import WebDriverException


class VideoPage(selenium.Page):
    __url_path__ = '/video/196391273929'

    active_menu = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class='sc-menu __reshare __noarrow sc-menu__top'
        )
    )

    @selenium.polling.wrap(timeout=20, delay=1)
    def wait_change(self):
        if u'Поделиться' in self.active_menu.text:
            raise WebDriverException(msg='Timeout at waiting video repost menu opened')

    def repost_video(self):
        self.browser.execute_script('''$(':button[tsid=reshareMenu]').last().click()''')
        self.active_menu.wait()
        self.browser.execute_script('''$("div[data-l*='t,now']").last().find('a').click()''')
        self.wait_change()
        return self.active_menu.text
