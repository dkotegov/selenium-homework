# coding=utf-8
from seismograph.ext import selenium

from pages.comment_page import CommentPage
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
        time.sleep(2)
        content = self.browser.find_elements_by_css_selector('div.feed')[0]
        return content

    def getAuthor(self,content):
        return content.find_elements_by_css_selector('span.shortcut-wrap')[0].find_elements_by_css_selector('a.o')[0], \
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


    def makeComment(self, content, feed_page):
        time.sleep(5)
        self.browser.execute_script('''$('div.feed_cnt').first().find('a.h-mod.widget_cnt').first().click()''')
        time.sleep(5)
        comment_body = CommentPage(feed_page.browser)
        comment_body.comment_input.set(u'hmm...')
        content.browser.find_elements_by_id('ok-e-d_button')[0].click()
        comment = comment_body.find_elements_by_css_selector('div.d_comment_w')[-1]
        comment_div = comment.find_element_by_css_selector('div.d_comment_text')
        if comment_div.text == 'hmm...':
            assert True
        else:
            assert False

    def makeSelfComment(self, content, feed_page):
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

    def makeLikeOnSelfComment(self, content, feed_page):
        button = content.browser.find_elements_by_css_selector('div.feed_f')[0].find_element_by_css_selector('a')
        button.click()
        comment_body = CommentPage(feed_page.browser)
        comment_body.comment_input.set(u'lel')
        content.browser.find_elements_by_id('ok-e-d_button')[0].click()
        comment = comment_body.find_elements_by_css_selector('div.d_comment_w')[-1]
        like_div = comment.find_element_by_css_selector('div.klass_w')
        like_div.click()
        like_div.click()
        like_div.click()
        if len(like_div.text) == 2:
            assert True
        else:
            assert False

    def makeDoubleLike(self, content, feed_page):
        button = content.browser.find_elements_by_css_selector('div.feed_f')[0].find_element_by_css_selector('a')
        button.click()
        comment_body = CommentPage(feed_page.browser)
        comment_body.comment_input.set(u'lel')
        content.browser.find_elements_by_id('ok-e-d_button')[0].click()
        comment = comment_body.find_elements_by_css_selector('div.d_comment_w')[-1]
        like_div = comment.find_element_by_css_selector('div.klass_w')
        like_div.click()
        like_div.click()
        like_div.click()
        like_div.click()
        if len(like_div.text) != 2:
            assert True
        else:
            assert False

    def makeLikeForSomemoneComment(self, content, feed_page):
        button = content.browser.find_elements_by_css_selector('div.feed_f')[0].find_element_by_css_selector('a')
        button.click()
        comment_body = CommentPage(feed_page.browser)
        comment = comment_body.find_elements_by_css_selector('div.d_comment_w')[-1]
        like_div = comment.find_element_by_css_selector('div.klass_w')
        like_div.click()
        like_div.click()
        like_div.click()
        if len(like_div.text) == 2:
            assert True
        else:
            assert False
            
    def makeRepost(self):
        self.popular_posts.wait()
        time.sleep(1)
        self.popular_posts.click()
        time.sleep(2)
        self.browser.execute_script('''$('div.feed_cnt').first().find('button.h-mod.widget_cnt').first().click()''')
        time.sleep(3)
        self.browser.execute_script('''$('div.feed').first().find("div[data-l*='t,now']").first().find('a').click()''')
        time.sleep(2)
        val = self.browser.find_elements_by_css_selector("span.tico")
        for a in val:
            if a.text == u'Опубликовано!':
                val = a.text
        return val

    def makeDoubleClickRepost(self):
        self.popular_posts.wait()
        time.sleep(1)
        self.popular_posts.click()
        self.browser.execute_script('''$('div.feed_cnt').first().find('button.h-mod.widget_cnt').first().click()''')
        time.sleep(3)
        self.browser.execute_script('''$('div.feed').first().find("div[data-l*='t,now']").first().find('a').dblclick()''')
        time.sleep(2)
        val = self.browser.find_elements_by_css_selector("span.tico")
        for a in val:
            if a.text == u'Опубликовано!':
                val = a.text
        return val

    def repostDoubleClick(self):
        return 1

    def makeLikeTwoLikes(self):
        time.sleep(5)
        val = self.browser.find_elements_by_css_selector('button.h-mod.widget_cnt')[-1].text

        self.browser.execute_script('''$('div.feed_cnt').first().find('button.h-mod.widget_cnt').last().click()''')
        self.browser.execute_script('''$('div.feed_cnt').first().find('button.h-mod.widget_cnt').last().click()''')

        new_val = self.browser.find_elements_by_css_selector('button.h-mod.widget_cnt')[-1].text

        if val == new_val:
            assert True
        else:
            assert False

        pass

    def makeOneLike(self):
        # может быть и false, если кто-то уберет лайк
        time.sleep(5)
        val = self.browser.find_element_by_css_selector('div.feed_cnt').find_elements_by_css_selector('button.h-mod.widget_cnt')[-1].text

        self.browser.execute_script('''$('div.feed_cnt').first().find('button.h-mod.widget_cnt').last().click()''')

        new_val = self.browser.find_element_by_css_selector('div.feed_cnt').find_elements_by_css_selector('button.h-mod.widget_cnt')[-1].text

        if val != new_val:
            assert True
        else:
            assert False

        pass

