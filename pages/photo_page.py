from seismograph.ext import selenium
from smth.xpath import XPathQueryObject

import time

class PhotoPage(selenium.Page):
    __url_path__ = '/pphotos/849451663773'

    avatar = selenium.PageElement(
        selenium.query(
            selenium.query.IMG,
            id='viewImageLinkId'
        )
    )

    def repostPhoto(self):
        return 1
