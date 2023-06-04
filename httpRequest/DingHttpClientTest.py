import unittest
from HttpClient import DingHttpClient


class MyTestCase(unittest.TestCase):
    def test_something(self):
        dingHttpClient = DingHttpClient()
        url = dingHttpClient.getImage('mIofN681YE3f/+m+NntqpQdM1+t4nRfOWJI1DXcCl4d/UMG6iyFLCn98f94j8fLjEvHAEsKMb45zfSG99e0BWNlC5A8+tbP4qCmqjUev+Io7n1SWB0jf/Tr8Pr/A8vxdx0yVZA5cz/7coRgYfou3Bt2pFN6+HAqqDmESyO1BSrvI1NOLFotmoLDX7b9NwAny',
                                            'dingn3zcecfk2kthtyvl')


if __name__ == '__main__':
    unittest.main()
