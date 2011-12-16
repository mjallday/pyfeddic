import mock
from mock import patch
import unittest

from pyfeddic.fedwire import FedWireRecord


class TestFedWire(unittest.TestCase):

    def test_load_from_file(self):
        record_string = ('113110641CITIZENS ST GANADO'
                         'CITIZENS STATE BANK        '
                         '         TXGANADO          '
                         '         YSN20100727')

        fwr = FedWireRecord(record_string)
        self.assertEqual(fwr.routing_number, '113110641')
