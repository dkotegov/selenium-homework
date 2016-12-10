# -*- coding: utf-8 -*-
import random

import time

from conf.base import OK_URL
from seismograph.ext import selenium
from utils.forms import AuthForm, NoteCreateForm
from utils.items import AddAudioPopup
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
    note_form.send_keys_in_last_text_form(note_texts[0])
    for i in range(1, note_texts_count + 1):
        note_form.controls.add_text_form()
        note_form.send_keys_in_last_text_form(note_texts[i])

    note_form.delete_last_added_text_form()

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


@suite.register
def test_create_with_photo(case, browser):
    pass


@suite.register
def test_create_with_audio(case, browser):
    """
        Выбираем случайным образом несколько аудиозаписей из поиска.
        Добавляем заметку, проверяем названия добавленных аудиозаписей.
        Проверяем возможность удаления аудиозаписи.
        Удаляем заметку.
    """

    _auth(browser)

    time.sleep(1)

    notes_page = NotesPage(browser)
    notes_page.open()
    notes_page.open_note_input()

    time.sleep(1)

    note_form = NoteCreateForm(browser)
    note_form.controls.add_audio()

    time.sleep(1)

    search_audio_name = u'Билан'
    add_audio_popup = AddAudioPopup(browser)
    add_audio_popup.search(search_audio_name)

    time.sleep(3)

    records_names = add_audio_popup.select_audio()

    time.sleep(1)

    add_audio_popup.add_audio()

    time.sleep(1)

    last_record_name = note_form.delete_last_added_audio()

    time.sleep(1)

    records_names.remove(last_record_name)

    note_form.in_status.unchecked()
    note_form.submit()

    time.sleep(1)

    expected_names = notes_page.get_last_note().get_audio_names()
    for name, expected_name in zip(sorted(records_names), sorted(expected_names)):
        case.assertion.is_in(name, expected_name)

    notes_page.get_last_note().delete()

    notes_page.refresh()
    time.sleep(1)

    with case.assertion.raises(IndexError):
        notes_page.get_last_note()
