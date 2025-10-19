import pygame
from constants import *
from load_board_data import tile_names

class Token(pygame.sprite.Sprite):
    """
    Represents a player's token (game piece) in the Monopoly game.
    """
    def __init__(self, Name, image_file):
        super().__init__()
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.name = Name
        self.current_position = 0 #use mod so that positions go from 0-31 incl but instead of 32, it goes back to 0
        self.rect.center = [square_w/2,square_h/2]
        self.money = 1200
        self.properties = []
        self.player_name = ''
        self.in_jail = False
        
    def add_property(self, property):
        self.properties.append(property)
    
    def move(self, spaces):
        target_position = (self.current_position + spaces) % 32
        self.rect.centerx = tile_center_x[target_position]
        self.rect.centery = tile_center_y[target_position]
        self.current_position = target_position
        
    def move_to_jail(self):
        self.rect.centerx = tile_center_x[tile_names.index('IN JAIL')]
        self.rect.centery = tile_center_y[tile_names.index('IN JAIL')]
        self.current_position = tile_names.index('IN JAIL')

