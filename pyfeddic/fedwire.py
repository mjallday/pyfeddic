"""
Pure Python Federal Reserve E-Payments Routing Directory Library.

@author: Marshall Jones <marshall at poundpay dot com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/lgpl.txt>.
"""


"""
## File format  - http://www.fedwiredirectory.frb.org/format.cfm
Field Name                                   Length Position

Routing number                                9     1-9
Telegraphic name                             18     10-27
Customer name                                36     28-63
State or territory abbreviation               2     64-65
City                                         25     66-90
Funds transfer status:                        1     91
    Y eligible
    N ineligible
Funds settlement-only status:                 1     92
    S settlement-only
Book-Entry Securities transfer status:        1     93
    N ineligible
    Y eligible
Date of last revision: YYYYMMDD, or blank     8     94-101

"""
from record import RecordBase, RecordFactory


class FedWireRecord(RecordBase):

    def __init__(self, line):
        assert len(line) >= 101
        self.routing_number = line[:9].strip()
        self.telegraphic_name = line[9:27].strip()
        self.customer_name = line[27:63].strip()
        self.state = line[63:65].strip()
        self.city = line[65:90].strip()
        self.funds_transfer_status = line[90].strip()
        self.funds_settlement_status = line[91].strip()
        self.securities_transfer_status = line[92].strip()
        self.date_of_last_revision = line[93:].strip() or None


class FedWire(RecordFactory):

    def __init__(self, location_of_db):
        super(self.__class__, self).__init__(location_of_db, FedWireRecord)
        self.load_db()

    def lookup_by_routing_number(self, routing_number):
        """
        Lookup corresponding ``FedWireRecord`` for a given ABA routing number.

        @param state: 9 digit routing number
        @type state: str
        @return: FedWireRecord
        @rtype: FedWireRecord
        """
        for record in self.records:
            if record.routing_number == routing_number:
                return record
        return None

    def lookup_by_state(self, state):
        """
        Lookup corresponding ``FedWireRecord``s for a given state.

        @param state: Two letter state code
        @type state: str
        @return: List of matching ``FedWireRecord``s
        @rtype: array
        """
        assert len(state) == 2
        return self.dynamic_record_lookup('state', state)
