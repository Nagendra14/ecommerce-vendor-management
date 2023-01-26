from abc import ABC, abstractmethod

class Vendor(ABC):
    
    @abstractmethod
    def login(self, username, password):
        """This method will be used to login an existing Vendor."""
        pass
    
    @abstractmethod
    def logout(self, username):
        """This method will be used to logout an existing Vendor."""
        pass