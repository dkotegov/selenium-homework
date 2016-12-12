from seismograph.ext import selenium


class OtherMenu(selenium.PageItem):
    __area__ = selenium.query(selenium.query.DIV, _class="mctc_navMenuDDC")

    holidays_link = selenium.PageElement(selenium.query(selenium.query.A, href="/holidays"),)

    go_to_holidays = selenium.PageElement(holidays_link, call=lambda we: we.click(),)


class NavMenu(selenium.PageItem):
    __area__ = selenium.query(selenium.query.DIV, _id="mctc_navMenu ")

    other = selenium.PageElement(OtherMenu)


class MainPage(selenium.Page):
    __url_path__ = "/feed/"

    nav_menu = selenium.PageElement(NavMenu)
