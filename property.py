from load_board_data import tile_names, tile_prices, tile_types, tile_rent
from constants import *

class Property:
    """
    This class stores information about a property, such as its name,
    position on the board and owner. It provides methods to 
    retrieve these attributes.
    """
    def __init__(self,Name):
        self.name = Name
        self.position = tile_names.index(str(Name)) #position is the same as the index of the property from board data file
        self.owner = None
    
    def get_rent(self):
        return tile_rent[self.position] #index is same as position
    
    def get_type(self):
        return tile_types[self.position]
    
    def get_price(self):
        return tile_prices[self.position]

