# -*- coding: utf-8 -*-

import time

from elements.forms import NoteCreateForm
from elements.items import NotePopup
from elements.pages import NotesPage
from seismograph.ext import selenium
from tests.notes.utils import auth, get_note_text


suite = selenium.Suite(__name__)


@suite.register
def test_comment(case, browser):
    """
        Добавляем заметку.
        Комментируем, проверяем возможность удаления / восстановления комментариев.
        Удаляем заметку.
    """

    auth(browser)

    notes_page = NotesPage(browser)
    notes_page.open()
    time.sleep(1)
    notes_page.remove_all_notes()

    notes_page.open_note_input()
    time.sleep(1)
    note_form = NoteCreateForm(browser)
    note_form.send_keys_in_last_text_form(get_note_text())
    note_form.in_status.unchecked()
    note_form.submit()
    time.sleep(2)

    comment_count = 3
    last_note = notes_page.get_last_note()
    last_note.open()
    time.sleep(1)
    note_popup = NotePopup(browser)
    for _ in range(comment_count):
        note_popup.comment_form.add_comment(get_note_text())
        time.sleep(1)
    case.assertion.equal(comment_count, note_popup.actions.get_comment_count())

    last_comment = note_popup.get_last_comment()
    last_comment.remove()
    time.sleep(1)
    case.assertion.equal(comment_count - 1, note_popup.actions.get_comment_count())

    note_popup.close()
    time.sleep(1)
    last_note = notes_page.get_last_note()
    case.assertion.equal(comment_count - 1, last_note.actions.get_comment_count())

    last_note.delete()
    time.sleep(1)

    notes_page.refresh()
    time.sleep(1)

    case.assertion.equal(0, notes_page.get_note_count())
