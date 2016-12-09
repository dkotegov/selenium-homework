from seismograph.ext import selenium
from smth.xpath import XPathQueryObject

import time

class VideoPage(selenium.Page):
    __url_path__ = '/video/196391273929'

    avatar = selenium.PageElement(
        selenium.query(
            selenium.query.IMG,
            id='viewImageLinkId'
        )
    )

    def repostVideo(self):
        return 1