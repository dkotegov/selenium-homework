import seismograph


suite = seismograph.Suite(__name__, require=['selenium'])


@suite.register
def selenium_example_1(case):
    pass


@suite.register
def selenium_example_2(case):
    pass
