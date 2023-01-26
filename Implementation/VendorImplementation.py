from Abstractions.Vendor import Vendor
from Models.VendorModel import VendorModel
from Models.VendorSessionModel import VendorSessionModel


class VendorImplementation(Vendor):

    def __init__(self):
        self.vendor_model = VendorModel()
        self.vendor_session = VendorSessionModel()

    def login(self, username, password):
        if self.vendor_model.is_correct_vendor(username, password):
            if self.vendor_session.login(username):
                print(f"User {username} logged in successfully")
                return True
        else:
            return False


    def logout(self, user_name):
        if self.vendor_session.check_login(user_name):
            if self.vendor_session.logout(user_name):
                print(f"User {user_name} logged out successfully.")
        else:
            print(f"{user_name} need to login first")
