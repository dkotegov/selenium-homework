# -*- coding: utf-8 -*-
import time

import seismograph
from elements.forms import NoteCreateForm
from elements.items import NotePopup
from elements.pages import NotesPage
from seismograph.ext import selenium
from tests.notes.base_steps import AuthStep, OpenNotesPageStep
from tests.notes.utils import get_note_text


suite = selenium.Suite(__name__)


@suite.register
class TestCommentNone(AuthStep, OpenNotesPageStep, selenium.Case):

    """
        Добавляем заметку.
        Комментируем, проверяем возможность удаления / восстановления комментариев.
        Удаляем заметку.
    """

    COMMENT_COUNT = 3

    @seismograph.step(3, 'Create note')
    def create_note(self, browser):
        notes_page = NotesPage(browser)
        notes_page.open_note_create_form()

        note_form = NoteCreateForm(browser)
        note_form.wait_for_open()
        note_form.send_keys_in_last_text_form(get_note_text())
        note_form.in_status.unchecked()
        note_form.submit()

        notes_page.wait_for_open()

    @seismograph.step(4, 'Comment note')
    def comment_note(self, browser):
        notes_page = NotesPage(browser)
        last_note = notes_page.get_last_note()
        last_note.open()

        note_popup = NotePopup(browser)
        for _ in range(self.COMMENT_COUNT):
            note_popup.comment_form.add_comment(get_note_text())
            # Добавляет комментарии слишком быстро
            time.sleep(0.5)

        self.assertion.equal(self.COMMENT_COUNT, note_popup.actions.get_comment_count())

    @seismograph.step(5, 'Check comment actions')
    def remove_comment(self, browser):
        notes_page = NotesPage(browser)
        note_popup = NotePopup(browser)

        last_comment = note_popup.get_last_comment()
        last_comment.remove()
        self.assertion.equal(self.COMMENT_COUNT - 1, note_popup.actions.get_comment_count())

        note_popup.close()
        notes_page.refresh()
        notes_page.wait_for_open()
        last_note = notes_page.get_last_note()
        self.assertion.equal(self.COMMENT_COUNT - 1, last_note.actions.get_comment_count())

    @seismograph.step(6, 'Remove note')
    def remove_note(self, browser):
        notes_page = NotesPage(browser)

        last_note = notes_page.get_last_note()
        last_note.delete()

        notes_page.refresh()
        notes_page.wait_for_open()

        self.assertion.equal(0, notes_page.get_note_count())
