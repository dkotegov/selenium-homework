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
        time.sleep(1)
        self.popular_posts.click()
        time.sleep(1)
        content = self.browser.find_elements_by_css_selector('div.feed')[0]
        return content

    def getAuthor(self,content):
        return content.find_elements_by_css_selector('span.shortcut-wrap')[0].find_elements_by_css_selector('a.o')[0],\
               content.find_elements_by_css_selector('span.shortcut-wrap')[0].find_elements_by_css_selector('a.o')[0].get_attribute('href')


    def getPost(self):
        return 1

    def makeLikeOnOwnPost(self):
        like_button = self.browser.find_elements_by_css_selector('button.h-mod.widget_cnt.controls-list_lk')[0]
        time.sleep(1)
        return like_button.click()

    def getStatusLikes(self):
        like_button = self.browser.find_elements_by_css_selector('button.h-mod.widget_cnt.controls-list_lk')[0]
        current_counter = int(like_button.find_elements_by_css_selector('span.widget_count')[0].text)
        return current_counter

    def makeRepost(self):
        # return self.browser.execute_script("$('[id*='hook_Block_ReshareNow_']')[0].click()")
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

