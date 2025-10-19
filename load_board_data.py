import json

# loads data from board_data.json 

board_data_JSON = open('board_data.json')

board_data_dict = json.load(board_data_JSON)

num_tiles = len(board_data_dict['boardData'])

tile_names = list(board_data_dict['boardData'][tile]['Name'] for tile in range(num_tiles))

tile_object_names = ['Free_Parking', 'Strand', 'Trafalgar_Sq', 'Fenchurch_St_Stn', 'Leicester_Sq', 'Coventry_St', 'Water_Works', 'Piccadilly', 
                     'GO_TO_JAIL', 'Regent_St', 'Oxford_St', 'Bond_St', 'Liverpool_St_Stn', 'Park_Ln', 'Super_Tax', 'Mayfair', 'GO', 'Old_Kent_Rd', 
                     'Whitechapel_Rd', 'Income_Tax', "Kings_Cross_Stn", 'The_Angel_Islington', 'Euston_Rd', 'Pentonville_Rd', 'IN_JAIL', 
                     'Electric_Company', 'Whitehall', 'Northumberland_Ave', 'Marylebone_Stn', 'Bow_St', 'Marlborough_St', 'Vine_St']

tile_prices = list(board_data_dict['boardData'][tile]['Price'] for tile in range(num_tiles))

tile_types = list(board_data_dict['boardData'][tile]['Type'] for tile in range(num_tiles))

tile_rent = list(board_data_dict['boardData'][tile]['Rent'] for tile in range(num_tiles))


