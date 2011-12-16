import urllib


class RecordBase(object):

    def __repr__(self):
        attrs = ', '.join(['%s=%s' % (k, repr(v)) for k, v in
                           self.__dict__.iteritems()])
        return '%s(%s)' % (self.__class__.__name__, attrs)


class RecordFactory(object):
    """Factory, yeah!"""

    def __init__(self, location_of_db, type_):
        self.records = []
        self._location_of_db = location_of_db
        self._type = type_

    def load_db(self):
        if self._location_of_db.find('://') >= 0:
            f = urllib.urlopen(self._location_of_db)
        else:
            f = open(self._location_of_db, 'r')

        for line in f:
            self.records.append(self._type(line))

    def dynamic_record_lookup(self, field, value):
        return [record for record in self.records
                if getattr(record, field, None) == value]
