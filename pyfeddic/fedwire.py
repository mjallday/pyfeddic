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
        for record in self.records:
            if record.routing_number == routing_number:
                return record
        return None

    def lookup_by_state(self, state):
        assert len(state) == 2
        return self.dynamic_record_lookup('state', state)
