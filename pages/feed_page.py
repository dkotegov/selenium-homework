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

    def getPopularContent(self):
        return self.popular_posts.click()

    def getAuthor(self):
        return 1

    def getPost(self):
        return 1

    def makeLikeOnOwnPost(self):
        return 1

    def makeComment(self):
        return 1

    def makeSelfComment(self):
        return 1

    def makeLikeOnSelfComment(self):
        return 1


    def makeLike(self):
        return 1

    def makeGroupComment(self):
        return 1

    def makeLikeForSomemoneComment(self):
        return 1

    def repostDoubleClick(self):
        return 1

