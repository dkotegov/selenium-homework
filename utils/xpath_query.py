from seismograph.ext import selenium
from seismograph.ext.selenium.exceptions import PollingTimeoutExceeded
from seismograph.ext.selenium.query import QueryObject, QueryResult
from seismograph.utils.common import waiting_for
from selenium.common.exceptions import NoSuchElementException, WebDriverException


class XPathQueryObject(QueryObject):
    def __init__(self, xpath, **selector):
        super(XPathQueryObject, self).__init__(selenium.query.ANY, **selector)
        self.xpath = xpath

    def __call__(self, proxy):
        return make_result(proxy, self.tag)(self.xpath)


class XPathQueryResult(QueryResult):
    def __init__(self, proxy, css):
        super(XPathQueryResult, self).__init__(proxy, css)
        self.__we = None

        self.__css = css
        self.__proxy = proxy

    def __repr__(self):
        return u'{}({}): {}'.format(
            self.__class__.__name__, self.__css, repr(self.__proxy),
        )

    def __getattr__(self, item):
        if not self.__we:
            self.first()
        return getattr(self.__we, item)

    @property
    def exist(self):
        """
        Check exist first element of query

        :rtype: bool
        """
        try:
            el = execute(self.__proxy, self.__css, disable_polling=True)

            if el:
                return True
            return False
        except WebDriverException:
            return False

    def wait(self, timeout=None, delay=None):
        """
        Wait for first element of query while timeout doesn't exceeded

        :param timeout: time for wait in seconds
        """
        return waiting_for(
            lambda: self.exist,
            exc_cls=PollingTimeoutExceeded,
            delay=delay or self.__proxy.config.POLLING_DELAY,
            timeout=timeout or self.__proxy.config.POLLING_TIMEOUT,
            message='Could not wait web element by xpath "{}"'.format(self.__css),
        )

    def get(self, index):
        """
        Get element of query by index

        :param index: index of element
        """
        try:
            self.__we = execute(self.__proxy, self.__css, list_result=True)[index]
            return self.__we
        except IndexError:
            raise NoSuchElementException(
                'Result does not have element by index "{}". XPath query: "{}".'.format(
                    index, self.__css,
                ),
            )

    def first(self):
        """
        Get first element of query
        """
        self.__we = execute(self.__proxy, self.__css)
        return self.__we

    def all(self):
        """
        Get all elements of query
        """
        return execute(self.__proxy, self.__css, list_result=True)


def make_result(proxy, tag):
    def handle(xpath):
        return XPathQueryResult(proxy, xpath)

    return handle


def get_execute_method(proxy, list_result):
    xpath_executors = {
        True: 'find_elements_by_xpath',
        False: 'find_element_by_xpath',
    }
    method_name = xpath_executors[bool(list_result)]

    return getattr(proxy, method_name)


def execute(proxy, xpath, list_result=False, disable_polling=False):
    proxy.reason_storage['last xpath query'] = xpath

    if disable_polling:
        with proxy.disable_polling():
            wait_timeout = proxy.config.WAIT_TIMEOUT
            proxy.config.WAIT_TIMEOUT = 0
            try:
                method = get_execute_method(proxy, list_result)
                result = method(xpath)
            finally:
                proxy.config.WAIT_TIMEOUT = wait_timeout
        return result

    method = get_execute_method(proxy, list_result)
    return method(xpath)
