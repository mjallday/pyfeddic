import mock
from mock import patch

from pyfeddic import FedWire
from pyfeddic.records import RecordFactory


class TestRecordFactory(object):

    def test_load_from_file(self):
        f = [1, 2, 3]
        path_to_file = '/path/to/file.txt'
        with mock.patch('pyfeddic.records.open', create=True) as mock_open:
            mock_open.return_value = mock.MagicMock(spec=f)

            rf = RecordFactory(path_to_file, None)
            rf.load_db()

        self.assertTrue(mock_open.call_count)
        args, _ = mock_open.call_args
        self.assertEqual(args[0], path_to_file)

    def test_load_from_url(self):
        url = 'http://www.example.com/file'
        with mock.patch('pyfeddic.records.urllib') as urllib:
            urllib.urlopen.return_value = mock.Mock()

            rf = RecordFactory(url)
            rf.load_db()

        self.assertTrue(urllib.call_count)
        args, _ = urllib.call_args
        self.assertEqual(args[0], url)
