# -*- coding: utf-8 -*-

from seismograph.ext import selenium
from elements import items
from elements.items import Note


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

    notes = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _tsid='userStatusShares'
        ),
        is_list=True,
        we_class=Note
    )

    def open_note_input(self):
        self.note_input.click()

    def get_last_note(self):
        return self.notes[0]

    def get_note(self, position):
        return self.notes[position]

    def get_note_count(self):
        return len(self.notes)
