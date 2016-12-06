from seismograph.ext import selenium
from utils.auth_manager import AuthManager
from utils.auth_pages import AuthPage
from utils.profile_page import ProfilePage


suite = selenium.Suite(__name__)

TEST_PROFILE_ID = '570965759077'


@suite.register
def test_add_five_plus_for_photo(case, browser):
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.auth(AuthManager.get_login(),
                   AuthManager.get_password())
    profile_page = ProfilePage(browser)
    profile_page.open(id=TEST_PROFILE_ID)
    profile_page.open_avatar()
    case.assertion.true(profile_page.is_five_plus_visible())
    profile_page.open_five_plus_payment()
    case.assertion.true(profile_page.is_five_plus_payment_open())


