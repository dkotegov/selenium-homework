# -*- coding: utf-8 -*-
import random

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

    text_content = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class='media-text_cnt_tx textWrap'
        )
    )

    audio_content = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class=selenium.query.contains('track_cnt')
        ),
        is_list=True
    )

    def get_text(self):
        return self.text_content.text

    def get_audio_names(self):
        return [record.text for record in self.audio_content]

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

    @staticmethod
    def _get_control(control_id):
        return \
            selenium.PageElement(
                selenium.query(
                    selenium.query.A,
                    id=selenium.query.contains(control_id)
                ),
                call=lambda btn: btn.click()
            )

    add_text_form = _get_control.__func__('opentext')

    add_photo = _get_control.__func__('openimage')

    add_audio = _get_control.__func__('openmusic')

    add_poll = _get_control.__func__('openpoll')


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


class NoteCreateFormAddedAudio(NoteCreateFormAddedElement):

    class AddedAudio(selenium.PageItem):

        # __area__ = selenium.query(
        #     selenium.query.SPAN,
        #     _class=selenium.query.contains('posting-form_track_info_w')
        # )

        info = selenium.PageElement(
            selenium.query(
                selenium.query.SPAN,
                _class=selenium.query.contains('posting-form_track_info')
            ),
            call=lambda field: field.text
        )

        delete_btn = selenium.PageElement(
            selenium.query(
                selenium.query.SPAN,
                _class=selenium.query.contains('posting-form_track_ac')
            )
        )

        def delete(self):
            with self.browser.action_chains as action:
                action.move_to_element(self)
                action.click(self.delete_btn)
                action.perform()

    audio_records = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class=selenium.query.contains('posting-form_track')
        ),
        is_list=True,
        we_class=AddedAudio
    )

    def delete_last(self):
        audio = self.audio_records[-1]
        info = audio.info()
        audio.delete()
        return info


class AddAudioPopup(selenium.PageItem):

    RECORDS_COUNT = 5

    __area__ = selenium.query(
        selenium.query.DIV,
        _class='modal-new_cnt'
    )

    search_input = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            _class=selenium.query.contains('search-input_it')
        )
    )

    audio_records = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class=selenium.query.contains('posting-form_track')
        ),
        is_list=True
    )

    add_audio = selenium.PageElement(
        selenium.query(
            selenium.query.A,
            _class=selenium.query.contains('form-actions_yes')
        ),
        call=lambda btn: btn.click()
    )

    def search(self, audio_name):
        self.search_input.send_keys(audio_name)

    def select_audio(self, count=RECORDS_COUNT):
        records = []
        for i in range(count):
            record = random.choice(self.audio_records)

            while record in records:
                record = random.choice(self.audio_records)

            records.append(record)

        for record in records:
            record.click()

        return [record.text for record in records]

