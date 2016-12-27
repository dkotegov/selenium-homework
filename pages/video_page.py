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

    @selenium.polling.wrap(delay=1)
    def wait_repost(self):
        self.browser.execute_script('''$("div[data-l*='t,now']").last().find('a').click()''')
        if u'Поделиться' in self.active_menu.text:
            raise WebDriverException(msg='Timeout at waiting video repost menu opened')

    def open_menu(self):
        self.browser.execute_script('''$(':button[tsid=reshareMenu]').last().click()''')
        self.active_menu.wait()

    def repost_video(self):
        self.wait_repost()
        return self.active_menu.text
