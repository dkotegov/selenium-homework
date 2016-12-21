# -*- coding: utf-8 -*-

from elements.forms import AuthForm

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

    footer = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            id='footer'
        )
    )

    def wait_for_open(self):
        self.footer.wait()


class AuthPage(BasePage):

    __url_path__ = '/'

    exit_link = None

    def authorize(self):
        auth_form = AuthForm(self.browser)
        auth_form.fill()
        auth_form.submit()


class UserPage(BasePage):

    avatar = selenium.PageElement(
        selenium.query(
            selenium.query.IMG,
            id='viewImageLinkId'
        )
    )

    def wait_for_open(self):
        while not self.avatar.is_displayed():
            pass


class NotesPage(BasePage):

    class StatusNote(selenium.PageItem):

        __area__ = selenium.query(
            selenium.query.DIV,
            _class=selenium.query.contains('media_feed_status')
        )

        get_text = selenium.PageElement(
            selenium.query(
                selenium.query.DIV,
                _class='media-text_cnt_tx'
            ),
            call=lambda field: field.text
        )

        remove_from_status_link = selenium.PageElement(
            selenium.query(
                selenium.query.A,
                _class='mst_close'
            )
        )

        def remove_from_status(self):
            with self.browser.action_chains as action:
                action.move_to_element(self)
                action.click(self.remove_from_status_link)
                action.perform()

    __url_path__ = '/statuses'

    note_input = selenium.PageElement(items.NoteInput)

    notes = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            tsid='userStatusShares'
        ),
        is_list=True,
        we_class=Note
    )

    status_note = selenium.PageElement(StatusNote, wait_timeout=2)

    def open_note_create_form(self):
        self.note_input.click()

    def get_last_note(self):
        return self.notes[0]

    def get_note(self, position):
        return self.notes[position]

    def get_note_count(self):
        return len(self.notes)

    def get_status_note(self):
        return self.status_note

    def remove_all_notes(self):
        for note in self.notes:
            note.delete()

    def restore_all_notes(self):
        for note in self.notes:
            note.restore()


class RemoveStatusPopup(selenium.PageItem):
    __area__ = selenium.query(
        selenium.query.DIV,
        _class='modal-new_hld'
    )

    submit = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            type='submit'
        ),
        call=lambda btn: btn.click()
    )
