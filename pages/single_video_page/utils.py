import seismograph
from seismograph.ext import selenium
from seismograph.ext.selenium.query import query as _query


class QueryUtil:

    TIMEOUT = 5

    def __init__(self, browser, query):
        self.browser = browser
        self.query = query

    def get_result(self):
        result = self.query(self.browser)
        result.wait(self.TIMEOUT)
        return result


class ScriptUtil:

    def __init__(self):
        pass

    @staticmethod
    def click_directly(driver, elem):
        driver.execute_script("arguments[0].click();", elem)

    @staticmethod
    def click_directly_seismograph(browser, seismograph_element):
        ScriptUtil.click_directly(browser._wrapped, seismograph_element._wrapped)

    @staticmethod
    def set_text_directly(driver, elem, text):
        driver.execute_script("arguments[0].innerHTML = '{}';".format(text), elem)

    @staticmethod
    def set_text_directly_seismograph(driver, elem, text):
        ScriptUtil.set_text_directly(driver._wrapped, elem._wrapped, text)



