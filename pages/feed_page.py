from seismograph.ext import selenium
from smth.xpath import XPathQueryObject
from repost_popup import RepostPage

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

    reshar_button = selenium.PageElement(
        selenium.query(
            selenium.query.BUTTON,
            _class='h-mod widget_cnt'
        )
    )

    reshar_button_selector = "button.h-mod.widget_cnt"

    make_reshar_div = selenium.PageElement(
        XPathQueryObject(
            '//div[@data-l="t,reshare-menu"]//div[@data-l="t,now"]'
        )
    )

    def getPopularContent(self):
        self.popular_posts.wait()
        self.popular_posts.click()
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

    def makeOwnRepost(self,content):
        self.reshar_button.click()
        self.make_reshar_div.wait()
        self.make_reshar_div.click()
        return 1

    def makeRepost(self):
        self.popular_posts.wait()
        time.sleep(1)
        self.popular_posts.click()
        self.browser.execute_script('''$('div.feed_cnt').first().find('button.h-mod.widget_cnt').first().click()''')
        time.sleep(3)
        self.browser.execute_script('''$('div.feed').first().find("div[data-l*='t,now']").first().find('a').click()''')
        time.sleep(2)
        val = self.browser.find_elements_by_css_selector("span.tico")[13].text
        return val

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

