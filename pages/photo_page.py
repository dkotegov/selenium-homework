from seismograph.ext import selenium


class PhotoPage(selenium.Page):
    first_album = selenium.PageElement(
        selenium.query(
            selenium.query.LI,
            _class='ugrid_i'
        )
    )

    check_opened_album = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class='photo-panel_info'
        )
    )

    new_album_button = selenium.PageElement(
        selenium.query(
            selenium.query.A,
            _class='portlet_h_ac lp'
        )
    )

    new_album_popup = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _id='mp_mm_cont',
        )
    )

    new_album_name_area = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            _id='field_photoAlbumName',
        )
    )

    new_album_save_button = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            _id='hook_FormButton_button_album_create',
        )
    )

    album_name = selenium.PageElement(
        selenium.query(
            selenium.query.SPAN,
            _class='photo-h_cnt_t ellip'
        )
    )

    first_photo = selenium.PageElement(
        selenium.query(
            selenium.query.A,
            _class='photo-card_cnt'
        )
    )

    close_button = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class='js-photoLayerClose ic photo-layer_close'
        )
    )

    photo = selenium.PageElement(
        selenium.query(
            selenium.query.IMG,
            id='__plpcte_target',
        )
    )

    next_arrow = selenium.PageElement(
        selenium.query(
            selenium.query.SPAN,
            _class='arw_ic'
        )
    )

    rotate_link = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            id='rotation-link-layer'
        )
    )

    image_0deg = selenium.PageElement(
        selenium.query(
            selenium.query.IMG,
            _class='photo-layer_img rotate__0deg'
        )
    )

    image_90deg = selenium.PageElement(
        selenium.query(
            selenium.query.IMG,
            _class='photo-layer_img rotate__90deg'
        )
    )

    image_180deg = selenium.PageElement(
        selenium.query(
            selenium.query.IMG,
            _class='photo-layer_img rotate__180deg'
        )
    )

    image_270deg = selenium.PageElement(
        selenium.query(
            selenium.query.IMG,
            _class='photo-layer_img rotate__270deg'
        )
    )

    link = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            _id='showLinkInput',
        )
    )

    delete_link = selenium.PageElement(
        selenium.query(
            selenium.query.A,
            _class='ic-w lp'
        )
    )

    restore_link = selenium.PageElement(
        selenium.query(
            selenium.query.A,
            _class='lp ml-2x'
        )
    )

    def open_first_album(self):
        self.first_album.click()
        self.check_opened_album.wait(timeout=3)

    def create_album(self, name):
        self.new_album_button.click()
        self.new_album_popup.wait(timeout=3)
        self.new_album_name_area.set(name)
        self.new_album_save_button.click()
        self.album_name.wait(timeout=3)

    def open_first_photo(self):
        self.first_photo.click()
        self.close_button.wait(timeout=3)

    def close_photo(self):
        self.close_button.wait(timeout=3)
        self.close_button.click()

    def next_photo(self):
        self.photo.wait(timeout=3)
        self.prev_size = self.photo.size
        self.next_arrow.wait(timeout=3)
        self.next_arrow.click()
        self.photo.wait(delay=3)

    def rotate_photo(self):
        self.photo.wait(timeout=3)
        if self.image_0deg.exist:
            self.rotate_link.click()
            self.image_90deg.wait(timeout=3)
            return self.image_90deg.exist
        elif self.image_90deg.exist:
            self.rotate_link.click()
            self.image_180deg.wait(timeout=3)
            return self.image_180deg.exist
        elif self.image_180deg.exist:
            self.rotate_link.click()
            self.image_270deg.wait(timeout=3)
            return self.image_270deg.exist
        elif self.image_270deg.exist:
            self.rotate_link.click()
            self.image_0deg.wait(timeout=3)
            return self.image_0deg.exist

    def delete_restore_photo(self):
        self.photo.wait(timeout=3)
        self.delete_link.wait(timeout=3)
        self.delete_link.click()
        self.restore_link.wait(timeout=3)
        if self.photo.is_displayed():
            self.restore_link.click()
            return False
        self.restore_link.click()
        self.photo.wait(delay=2)
