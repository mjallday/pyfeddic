import mock
from mock import patch
import unittest

from pyfeddic.record import RecordFactory


class TestRecordFactory(unittest.TestCase):

    def test_load_from_file(self):
        path_to_file = '/path/to/file.txt'
        f = [1, 2, 3]

        with mock.patch('pyfeddic.record.open', create=True) as mock_open:
            mock_open.return_value = f

            rf = RecordFactory(path_to_file, mock.Mock())
            rf.load_db()

        self.assertTrue(mock_open.call_count)
        args, _ = mock_open.call_args
        self.assertEqual(args[0], path_to_file)
        self.assertEqual(len(rf.records), len(f))

    def test_load_from_url(self):
        url = 'http://www.example.com/file'
        f = [1, 2, 3]

        with mock.patch('pyfeddic.record.urllib') as urllib:
            urllib.urlopen.return_value = f

            rf = RecordFactory(url, mock.Mock())
            rf.load_db()

        self.assertEqual(urllib.urlopen.call_count, 1)
        args, _ = urllib.urlopen.call_args
        self.assertEqual(args[0], url)
        self.assertEqual(len(rf.records), len(f))

    def test_dyanmic_lookup(self):
        class WithAProperty(object):
            def __init__(self, value):
                self.property = value

        records = [WithAProperty('one'), WithAProperty('two'),
                   WithAProperty('one')]
        rf = RecordFactory(None, None)
        rf.records = records

        filtered = rf.dynamic_record_lookup('property', 'one')
        self.assertEqual(len(filtered), 2)

        filtered = rf.dynamic_record_lookup('nothing', 'one')
        self.assertEqual(len(filtered), 0)
