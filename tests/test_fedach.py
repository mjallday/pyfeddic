import mock
from mock import patch
import unittest

from pyfeddic.fedach import FedACHRecord


class TestFedWire(unittest.TestCase):

    def test_load_from_file(self):
        record_string = ('121000536O1210003742010504122000030BANK OF AMERICA,'
                         ' N.A.               PO BOX 27025                   '
                         '     RICHMOND            VA232617025800446013511     ')

        fwr = FedACHRecord(record_string)
        self.assertEqual(fwr.routing_number, '121000536')
        self.assertEqual(len(fwr.telephone), 3 + 3 + 4)
