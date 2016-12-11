from seismograph.ext import selenium
from seismograph.ext.selenium import PageItem
from seismograph.ext.selenium import PageElement
from seismograph.ext.selenium import query
from pages.single_video_page.utils import ScriptUtil


class AttachVideoDialog(PageItem):

    __area__ = query(
        query.DIV,
        _id='hook_Block_AttachShareVideoContent'
    )

    class Video(PageItem):

        def click_video(self):
            self.we.click()

    el_video = PageElement(
        query(
            query.A,
            _class=query.contains('vid-card vid-card__l attachInput')
        ),
        we_class=Video
    )
