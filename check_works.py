import seismograph
from seismograph.ext import selenium

suite = selenium.Suite(__name__)


@suite.register
def my_first_test(case):
    case.assertion.equal(1, 1)


if __name__ == '__main__':
    seismograph.main()
