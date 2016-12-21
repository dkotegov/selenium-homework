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


class NoteActions(selenium.PageItem):

    class LikeButton(selenium.PageItem):

        __area__ = selenium.query(
            selenium.query.BUTTON,
            _class=selenium.query.contains('controls-list_lk')
        )

        get_like_count = selenium.PageElement(
            selenium.query(
                selenium.query.SPAN,
                _class='widget_count'
            ),
            call=lambda field: int(field.text)
        )

    class CommentButton(selenium.PageItem):

        get_comment_count = selenium.PageElement(
            selenium.query(
                selenium.query.SPAN,
                _class=selenium.query.contains('widget_count')
            ),
            call=lambda field: int(field.text)
        )

    __area__ = selenium.query(
        selenium.query.UL,
        _class='widget-list'
    )

    like_btn = selenium.PageElement(LikeButton)

    comment_btn = selenium.PageElement(
        selenium.query(
            selenium.query.LI,
            _class='widget-list_i'
        ),
        index=0,
        we_class=CommentButton
    )

    def like(self):
        self.like_btn.click()

    def unlike(self):
        self.like_btn.click()

    def get_like_count(self):
        return self.like_btn.get_like_count()

    def comment(self):
        self.comment_btn.click()

    def get_comment_count(self):
        return self.comment_btn.get_comment_count()


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
            _class=selenium.query.contains('media-text_cnt_tx')
        )
    )

    audio_content = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class=selenium.query.contains('track_cnt')
        ),
        is_list=True
    )

    photo_content = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class='collage_i'
        ),
        is_list=True
    )

    place_header = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class='feed_h'
        )
    )

    maps = selenium.PageElement(
        selenium.query(
            selenium.query.A,
            _class='media-map_a'
        ),
        is_list=True
    )

    restore_link = selenium.PageElement(
        selenium.query(
            selenium.query.A,
            _class=selenium.query.contains('delete-stub_cancel')
        )
    )

    in_status_link = selenium.PageElement(
        selenium.query(
            selenium.query.SPAN,
            _class='tico'
        )
    )

    actions = selenium.PageElement(NoteActions)

    def open(self):
        self.text_content.click()

    def get_text(self):
        return self.text_content.text

    def get_audio_names(self):
        return [record.text for record in self.audio_content]

    def get_photo_count(self):
        return len(self.photo_content)

    def get_place_names(self):
        return self.place_header.text

    def get_map_count(self):
        return len(self.maps)

    def delete(self):
        with self.browser.action_chains as action:
            action.move_to_element(self)
            action.click(self.delete_btn)
            action.perform()
        self.restore_link.wait()

    def restore(self):
        self.restore_link.click()

    def in_status(self):
        with self.browser.action_chains as action:
            action.move_to_element(self)
            action.click(self.in_status_link)
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

    class AddImageBtn(selenium.PageItem):

        __area__ = selenium.query(
            selenium.query.A,
            id=selenium.query.contains('openimage')
        )

        file_input = selenium.PageElement(
            selenium.query(
                selenium.query.INPUT,
                _class='html5-upload-link'
            )
        )

    add_text_form = _get_control.__func__('opentext')

    add_photo = selenium.PageElement(
        AddImageBtn,
        call=lambda btn, file_name: btn.file_input.send_keys(file_name)
    )

    add_audio = _get_control.__func__('openmusic')

    add_poll = _get_control.__func__('openpoll')


class NoteCreateFormActions(selenium.PageItem):

    __area__ = selenium.query(
        selenium.query.DIV,
        _class='form-actions'
    )

    add_place = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            uid='plBtn'
        ),
        call=lambda btn: btn.click()
    )

    add_user = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            uid='wfBtn'
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


class NoteCreateFormAddedAudio(NoteCreateFormAddedElement):

    class AddedAudio(selenium.PageItem):

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


class NoteCreateFormAddedPhoto(NoteCreateFormAddedElement):

    class AddedPhoto(selenium.PageItem):

        delete_btn = selenium.PageElement(
            selenium.query(
                selenium.query.DIV,
                id=selenium.query.contains('remove')
            )
        )

        def delete(self):
            with self.browser.action_chains as action:
                action.move_to_element(self)
                action.click(self.delete_btn)
                action.perform()

    photos = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            id=selenium.query.contains('preview')
        ),
        is_list=True,
        we_class=AddedPhoto
    )

    def delete_last_inside_block(self):
        self.photos[-1].delete()


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


class NoteCreateFormPlaceSelect(selenium.PageItem):

    class Place(selenium.PageItem):

        get_name = selenium.PageElement(
            selenium.query(
                selenium.query.DIV,
                _class=selenium.query.contains('ucard_info_name'),
            ),
            call=lambda field: field.text
        )

    class SelectedPlace(selenium.PageItem):

        __area__ = selenium.query(
            selenium.query.DIV,
            _class='pform_map_search_result'
        )

        get_name = selenium.PageElement(
            selenium.query(
                selenium.query.SPAN,
                uid='plc'
            ),
            call=lambda field: field.text
        )

        remove = selenium.PageElement(
            selenium.query(
                selenium.query.DIV,
                id=selenium.query.contains('PlaceSelctionRemove')
            ),
            call=lambda btn: btn.click()
        )

    search_input = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            id=selenium.query.contains('PlaceSearchInput')
        )
    )

    place_list = selenium.PageElement(
        selenium.query(
            selenium.query.LI,
            _class='suggest_li',
        ),
        is_list=True,
        we_class=Place
    )

    selected_place = selenium.PageElement(SelectedPlace)

    def search(self, place_name):
        self.search_input.send_keys(place_name)

    def select_random_place(self):
        random_place = random.choice(self.place_list)
        place_name = random_place.get_name()
        random_place.click()
        return place_name

    def select_first_place(self):
        first_place = self.place_list[0]
        place_name = first_place.get_name()
        first_place.click()
        return place_name

    def remove_selected_place(self):
        self.selected_place.remove()


class NoteCreateFormUserSelect(selenium.PageItem):

    class User(selenium.PageItem):
        __area__ = selenium.query(
            selenium.query.DIV,
            _class=selenium.query.contains('ucard-mini')
        )

        get_name = selenium.PageElement(
            selenium.query(
                selenium.query.DIV,
                _class='ucard-mini_cnt_i ellip'
            ),
            call=lambda field: field.text
        )

    class SelectUser(selenium.PageItem):

        get_name = selenium.PageElement(
            selenium.query(
                selenium.query.ANY,
                dir='ltr'
            ),
            call=lambda tag: tag.text
        )

        remove = selenium.PageElement(
            selenium.query(
                selenium.query.ANY,
                uid='rm'
            ),
            call=lambda btn: btn.click()
        )


    search = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            id=selenium.query.contains('wfid-input')
        ),
        call=lambda input, text: input.send_keys(text)
    )

    return_to_friend_list = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            uid='sl'
        ),
        call=lambda link: link.click()
    )

    user_list = selenium.PageElement(
        selenium.query(
            selenium.query.LI,
            _class='suggest_li'
        ),
        is_list=True,
        we_class=User
    )

    selected_users = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class='tag'
        ),
        is_list=True,
        we_class=SelectUser
    )

    def remove_last_user(self):
        self.selected_users[-1].remove()

    def select_user(self, position):
        user = self.user_list[position]
        user_name = user.get_name()
        user.click()
        return user_name


class NotePopup(selenium.PageItem):

    class CommentForm(selenium.PageItem):

        __area__ = selenium.query(
            selenium.query.DIV,
            _class=selenium.query.contains('comments_form')
        )

        add_comment_button = selenium.PageElement(
            selenium.query(
                selenium.query.BUTTON,
                _class=selenium.query.contains('form-actions_yes')
            )
        )

        comment_input = selenium.PageElement(
            selenium.query(
                selenium.query.DIV,
                _class=selenium.query.contains('comments_add-ceditable')
            )
        )

        def add_comment(self, text):
            self.comment_input.send_keys(text)
            self.add_comment_button.click()

    class Comment(selenium.PageItem):

        remove_btn = selenium.PageElement(
            selenium.query(
                selenium.query.A,
                _class=selenium.query.contains('comments_remove')
            )
        )

        restore = selenium.PageElement(
            selenium.query(
                selenium.query.A,
                _class=selenium.query.contains('delete-stub_cancel')    # TODO: Почему-то не видит :(
            ),
            call=lambda btn: btn.click()
        )

        def remove(self):
            with self.browser.action_chains as action:
                action.move_to_element(self)
                action.click(self.remove_btn)
                action.perform()

    class ActionsMenu(selenium.PageItem):

        def edit(self):
            self.browser.execute_script('$(".ic_edit").click();')

        # TODO: Неуловимое выпадающее меню
        """
        edit = selenium.PageElement(
            selenium.query(
                selenium.query.ANY,
                _class=selenium.query.contains('ic_edit')
            ),
            call=lambda btn: btn.click()
        )
        """

    __area__ = selenium.query(
        selenium.query.DIV,
        _class='media-layer_hld'
    )

    close = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class=selenium.query.contains('media-layer_close_ico')
        ),
        call=lambda btn: btn.click()
    )

    get_friends_names = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class='media_company textWrap'
        ),
        call=lambda field: field.text
    )

    actions = selenium.PageElement(NoteActions)

    comment_form = selenium.PageElement(CommentForm)

    comments = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class=selenium.query.contains('comments_current')
        ),
        is_list=True,
        we_class=Comment
    )

    actions_menu_dropdown = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class=selenium.query.contains('ic12_arrow-down')
        )
    )

    actions_menu = selenium.PageElement(ActionsMenu)

    text_input = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            id='0#0.posting_form_text_field'
        )
    )

    submit = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            type='submit'
        ),
        call=lambda btn: btn.click()
    )

    def wait_for_open(self):
        self.comment_form.wait()

    def edit_note(self, text):
        import time
        self.actions_menu_dropdown.click()
        self.actions_menu.edit()
        time.sleep(1)
        with self.browser.action_chains as action:
            action.move_to_element(self.text_input)
            action.click(self.text_input)
            action.perform()
        self.text_input.send_keys(text)
        time.sleep(1)
        self.submit()

    def get_last_comment(self):
        return self.comments[-1]
