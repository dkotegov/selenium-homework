import seismograph

__all__ = [
    'program'
]


class SeleniumProgram(seismograph.Program):

    def setup(self):
        with self.ext('selenium') as browser:
            browser.go_to('http://google.com')

    def teardown(self):
        pass


program = SeleniumProgram(config_path='conf.base', require=['selenium'])
