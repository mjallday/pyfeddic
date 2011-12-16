from __future__ import unicode_literals


from fedach import FedACH
from fedwire import FedWire


def main():
    parser = optparse.OptionParser()
    parser.add_option('--dry-run', '-d', default=False,
                      action='store_true', help='Dry run')
    parser.add_option('--client', '-c',
        default='BankOfAmericaACHClient',
        help='Defaults to the BankOfAmericaACHClient. \nHere are the list '
            'of clients: %s' % pprint.pformat(ACH_CLIENT_LIST))
    options, args = parser.parse_args()

    fw = FedWire('/Users/Marsh/Downloads/fpddir.txt')
    print len(fw.records)
    print fw.lookup_by_routing_number('121000374')
#    print fw.lookup_by_state('CA')
#    print len(FedWire('http://www.fedwiredirectory.frb.org/fpddir.txt').records)


if __name__ == '__main__':
    main()
