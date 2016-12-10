# -*- coding: utf-8 -*-
import random

import time

from conf.base import OK_URL
from seismograph.ext import selenium
from utils.forms import AuthForm, NoteCreateForm
from utils.pages import NotesPage


suite = selenium.Suite(__name__)


def _auth(browser):
    browser.go_to(OK_URL)

    auth_form = AuthForm(browser)
    auth_form.fill()
    auth_form.submit()


def _get_note_text():
    return u'TEST NOTE - ТЕСТОВАЯ ЗАМЕТКА - {0}'.format(random.randint(0, 1000))


@suite.register
def test_create_with_text_boxes(case, browser):
    """
        Заполняем случайным образом несколько текстовых форм.
        Удаляем одну из форм.
        Добавляем заметку, проверяем получившейся в ней текст.
        Удаляем заметку.
    """

    note_texts_count = 3

    _auth(browser)

    time.sleep(1)

    notes_page = NotesPage(browser)
    notes_page.open()
    notes_page.open_note_input()

    time.sleep(1)

    note_texts = []
    for i in range(0, note_texts_count + 2):
        note_texts.append(_get_note_text())

    note_form = NoteCreateForm(browser)
    note_form.send_keys_in_last_text_input(note_texts[0])
    for i in range(1, note_texts_count + 1):
        note_form.controls.add_text_input()
        note_form.send_keys_in_last_text_input(note_texts[i])

    note_form.delete_last_added_text_input()

    time.sleep(1)

    note_form.in_status.unchecked()
    note_form.submit()

    time.sleep(1)

    note_final_text = '\n'.join(note_texts[:-2])
    case.assertion.equal(notes_page.get_last_note().get_text(), note_final_text)

    notes_page.get_last_note().delete()

    notes_page.refresh()
    time.sleep(1)

    with case.assertion.raises(IndexError):
        notes_page.get_last_note()
