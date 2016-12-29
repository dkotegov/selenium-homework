from seismograph.ext import selenium


class AlbumPage(selenium.Page):
    album = selenium.PageElement(
        selenium.query(
            selenium.query.LI,
            _class='ugrid_i'
        )
    )

    edit = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class='photo-menu_edit iblock-cloud_show'
        )
    )

    delete = selenium.PageElement(
        selenium.query(
            selenium.query.LI,
            _class='controls-list_item'
        )
    )

    confirm_delete = selenium.PageElement(
        selenium.query(
            selenium.query.INPUT,
            _id='hook_FormButton_button_delete_confirm',
        )
    )

    add_album = selenium.PageElement(
        selenium.query(
            selenium.query.SPAN,
            _class='add-stub_tx'
        )
    )

    def delete_album(self):
        self.album.wait(timeout=3)
        self.album.get(3).click()
        self.edit.wait(timeout=3)
        self.edit.click()
        self.delete.wait(timeout=3)
        self.delete.get(1).click()
        self.confirm_delete.wait(timeout=3)
        self.confirm_delete.click()
        self.add_album.wait(timeout=3)
        return self.add_album.exist



