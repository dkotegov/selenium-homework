import seismograph


suite = seismograph.Suite(__name__, require=['selenium'])


@suite.register
def selenium_example(case):
    pass
