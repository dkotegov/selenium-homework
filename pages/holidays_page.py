from seismograph.ext import selenium


class HolidaysPage(selenium.Page):
    __url_path__ = "/holidays"

    my_holidays_link = selenium.PageElement(selenium.query(selenium.query.A, href="/holidays/my"),)

    go_to_my_holidays = selenium.PageElement(my_holidays_link, call=lambda we: we.click(),)

    
