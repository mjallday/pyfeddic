"""
## File Format - http://www.fedwiredirectory.frb.org/format_ACH.cfm

Field Name                     Length Position  Description
Routing Number                 9     1-9        The institution's routing number
Office Code                    1     10         Main office or branch O=main B=branch
Servicing FRB Number           9     11-19      Servicing Fed's main office routing number
Record Type Code               1     20         The code indicating the ABA number to be used to route or send ACH items to the RFI
    0 = Institution is a Federal Reserve Bank
    1 = Send items to customer routing number
    2 = Send items to customer using new routing number field
Change Date                    6     21-26       Date of last change to CRF information (MMDDYY)
New Routing Number             9     27-35       Institution's new routing number resulting from a merger or renumber
Customer Name                 36     36-71       Commonly used abbreviated name
Address                       36     72-107      Delivery address
City                          20     108-127     City name in the delivery address
State Code                     2     128-129     State code of the state in the delivery address
Zipcode                        5     130-134     Zip code in the delivery address
Zipcode Extension              4     135-138     Zip code extension in the delivery address
Telephone Area Code            3     139-141     Area code of the CRF contact telephone number
Telephone Prefix Number        3     142-144     Prefix of the CRF contact telephone number
Telephone Suffix Number        4     145-148     Suffix of the CRF contact telephone number
Institution Status Code        1     149     Code is based on the customers receiver code
1=Receives Gov/Comm
Data View Code                 1     150     1=Current view
Filler                         5     151-155     Spaces

"""
from record import RecordBase, RecordFactory


class FedACHRecord(RecordBase):

    def __init__(self, line):
        assert len(line) >= 150
        self.routing_number = line[:9].strip()
        self.office_code = line[10].strip()
        self.servicing_frb_number = line[10:19].strip()
        self.record_type_code = line[19].strip()
        self.change_date = line[20:26].strip()
        self.new_routing_number = line[26:35].strip()
        self.customer_name = line[35:71].strip()
        self.address = line[71:107].strip()
        self.city = line[107:127].strip()
        self.state = line[127:129].strip()
        self.zip_code = line[129:134].strip()
        self.zip_code_extension = line[134:138].strip()
        self.telephone = line[138:148].strip()
        self.institution_status_code = line[148].strip()
        self.data_view_code = line[149].strip()


class FedACH(RecordFactory):

    def __init__(self, location_of_db):
        super(self.__class__, self).__init__(location_of_db, FedACHRecord)
        self.load_db()
