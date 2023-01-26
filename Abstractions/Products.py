from abc import ABC, abstractmethod

class Products(ABC):
    
    @abstractmethod
    def add_product(self, product_name, product_type, available_quantity, unit_price):
        """This abstract method will be used to add products"""
        pass
    
    @abstractmethod
    def search_product_by_name(self, product_name):
        """This abstract method will be used to search for products by name."""
        pass
    
    @abstractmethod
    def get_all_products(self):
        """This abstract method will be used to search for products by name."""
        pass
