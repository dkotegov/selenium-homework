# -*- coding: utf-8 -*-

from seismograph.ext import selenium


class BasePage(selenium.Page):

    exit_link = selenium.PageElement(
        selenium.query(
            selenium.query.A,
            _href='/feed',
            value=u'Выход'
        ),
    )
