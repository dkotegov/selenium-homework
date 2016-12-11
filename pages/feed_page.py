# coding=utf-8
from seismograph.ext import selenium

from pages.comment_page import CommentPage
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

    def makeRepost(self):
        # return self.browser.execute_script("$('[id*='hook_Block_ReshareNow_']')[0].click()")
        return 1

    def makeComment(self, content, feed_page):
        button = content.browser.find_elements_by_css_selector('div.feed_f')[0].find_element_by_css_selector('a')
        button.click()
        comment_body = CommentPage(feed_page.browser)
        comment_body.comment_input.set(u'lel')
        content.browser.find_elements_by_id('ok-e-d_button')[0].click()
        comment = comment_body.find_elements_by_css_selector('div.d_comment_w')[-1]
        comment_div = comment.find_element_by_css_selector('div.d_comment_text')
        if comment_div.text == 'lel':
            assert True
        else:
            assert False


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

