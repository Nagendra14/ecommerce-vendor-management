import csv

VENDOR_FILE = "C:/Users/Call me X/Downloads/iiith/OOP's/M01-W01-02-Ecommerce+vendor+management/Ecommerce vendor management/config/vendor.csv"


class VendorModel:

    def __init__(self):
        self.vendor_db = []
        self.__login_data = dict()
        self._load_vendors()

    # loading all the vendors from the csv file. 
    # Do not edit anything

    def _load_vendors(self):
        csv_data = csv.DictReader(open(VENDOR_FILE))
        for vendor in csv_data:
            self.vendor_db.append(vendor)
            self.__login_data[vendor["User Name"]] = vendor["Password"]

    # Checking if the vendor exist in the dictionary after all the vendor info is loaded. 
    # Do not edit anything
    def is_correct_vendor(self, username, password):
        if (username in self.__login_data):
            if (self.__login_data[username] == password):
                return True
            else:
                return False
        else:
            return False
