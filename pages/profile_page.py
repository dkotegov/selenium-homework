from seismograph.ext import selenium


class ProfilePage(selenium.Page):
    __url_path__ = '/profile/{id}'

    avatar = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _class='lcTc_avatar __l',
        )
    )

    full_width_avatar = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _id='photo-layer_img_w',
        )
    )

    five_plus_button = selenium.PageElement(
        selenium.query(
            selenium.query.A,
            _class='marks-new_ic __plus',
        )
    )

    five_plus_iframe = selenium.PageElement(
        selenium.query(
            selenium.query.DIV,
            _id='pmntWzrdCtr',
        )
    )

    def open_avatar(self):
        ava = self.avatar.a(_class='card_wrp')
        ava.wait()
        ava.click()
        self.full_width_avatar.wait(timeout=2)

    def is_five_plus_visible(self):
        return self.five_plus_button.exist

    def open_five_plus_payment_from_photo(self):
        self.five_plus_button.click()

    def is_five_plus_payment_open(self):
        self.five_plus_iframe.wait(timeout=3)
        return self.five_plus_iframe.exist
