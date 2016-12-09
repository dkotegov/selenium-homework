# -*- coding: utf-8 -*-

from seismograph.ext import selenium
from utils import items


class BasePage(selenium.Page):

    exit_link = selenium.PageElement(
        selenium.query(
            selenium.query.A,
            _href='/feed',
            value=u'Выход'
        ),
    )


class NotesPage(BasePage):

    __url_path__ = '/statuses'

    note_input = selenium.PageElement(items.NoteInput)

    def open_note_input(self):
        self.note_input.click()
