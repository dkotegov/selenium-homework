# -*- coding: utf-8 -*-

from seismograph.ext import selenium


class NoteInput(selenium.PageItem):

    __area__ = selenium.query(
        selenium.query.DIV,
        id='hook_Block_PostingForm',
    )


class InStatusCheckbox(selenium.PageItem):

    __area__ = selenium.query(
        selenium.query.DIV,
        _class='posting-form_ac-status'
    )

    unchecked = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            _class='irc',
        ),
        call=lambda checkbox: checkbox.click()
    )


class Note(selenium.PageItem):

    delete_btn = selenium.PageElement(
        selenium.query(
            selenium.query.A,
            _class="al feed_close"
        )
    )

    text_field = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class='media-text_cnt_tx textWrap'
        )
    )

    def get_text(self):
        return self.text_field.text

    def delete(self):
        with self.browser.action_chains as action:
            action.move_to_element(self)
            action.click(self.delete_btn)
            action.perform()


class NoteCreateFormControls(selenium.PageItem):

    __area__ = selenium.query(
        selenium.query.DIV,
        _class=selenium.query.contains('posting-form_controls__active'),
    )

    add_text_input = selenium.PageElement(
        selenium.query(
            selenium.query.A,
            id=selenium.query.contains('opentext')
        ),
        call=lambda btn: btn.click()
    )


class NoteCreateFormAddedElement(selenium.PageItem):
    """
        Text, photo, music, etc.

    """

    delete_btn = selenium.PageElement(
        selenium.query(
            selenium.query.SPAN,
            id=selenium.query.contains('close')
        )
    )

    def delete(self):
        with self.browser.action_chains as action:
            action.move_to_element(self)
            action.click(self.delete_btn)
            action.perform()


class NoteCreateFormAddedText(NoteCreateFormAddedElement):

    text_input = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class=selenium.query.contains('textWrap')
        ),
    )
