import seismograph
from seismograph.ext import selenium

from conf.base_config import LOGIN, PASSWORD
from pages.auth_page import AuthPage
from pages.holidays_page import HolidaysPage

suite = selenium.Suite(__name__)


class AuthStep(selenium.Case):
    @seismograph.step(1, "Log in to Ok.ru")
    def auth(self, browser):
        auth_page = AuthPage(browser)
        auth_page.open()
        auth_page.log_in(LOGIN, PASSWORD)


@suite.register
class HolidaysModalTestCase(AuthStep, selenium.Case):
    @seismograph.step(2, "Assert holiday's modal window is opening.")
    def test_modal_opens(self, browser):
        holidays_page = HolidaysPage(browser)
        holidays_page.open()
