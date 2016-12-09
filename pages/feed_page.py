from seismograph.ext import selenium
from smth.xpath import XPathQueryObject

import time


class FeedPage(selenium.Page):
    __url_path__ = '/feed'

    avatar = selenium.PageElement(
        selenium.query(
            selenium.query.IMG,
            id='viewImageLinkId'
        )
    )

    popular_posts = selenium.PageElement(
        XPathQueryObject(
            '//a[@data-l="feedTargetFilterId,777"]'
        )
    )

    friends_posts = selenium.PageElement(
        XPathQueryObject(
            '//a[@data-l="feedTargetFilterId,301"]'
        )
    )

