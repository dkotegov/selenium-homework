from seismograph.ext import selenium


class HolidaysModal(selenium.PageItem):
    __area__ = selenium.query(selenium.query.DIV, _id="popLayerBodyWrapper")

    add_self_holiday_btn = selenium.PageElement(selenium.query.SPAN, _class="pay-tab_name")


class MyHolidaysPage(selenium.Page):
    __url_path__ = "/holidays/my"

    __area__ = selenium.query(selenium.query.DIV, _id="middleColumn",)

    add_holiday_btn = selenium.PageElement(selenium.query(selenium.query.INPUT, id="hook_FormButton_button_create"),)

