from seismograph.ext import selenium
from seismograph.ext.selenium import PageItem
from seismograph.ext.selenium import PageElement
from seismograph.ext.selenium import query


class PageItemBase(PageItem):

    def __init__(self, browser, *args, **kwargs):
        super(PageItem, self).__init__(*args, **kwargs)
        self.browser = browser
