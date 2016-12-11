from seismograph.ext import selenium
from seismograph.ext.selenium import PageItem
from seismograph.ext.selenium import PageElement
from seismograph.ext.selenium import query
from pages.single_video_page.utils import ScriptUtil


class MinimizedVideo(PageItem):

    __area__ = query(
        query.DIV,
        _class=query.contains('vp-modal')
    )

    el_maximize = PageElement(
        query(
            query.SPAN,
            _class=query.contains('__roll-out')
        )
    )

    el_close = PageElement(
        query(
            query.SPAN,
            _class=query.contains('__close')
        )
    )

    def maximize(self):
        self.el_maximize.we.click()

    def close(self):
        self.el_close.we.click()
