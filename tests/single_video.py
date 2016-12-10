import seismograph
from base_case import BaseCase

suite = seismograph.Suite(__name__, require=['selenium'])

@suite.register
class Test1Case(BaseCase):
