import pygame
from constants import *

class Button:
    """
    This class handles rendering a rectangular button with text, centring the text
    within the button, and detecting mouse clicks on the button.
    """
    def __init__(self, Screen, Width, Height, Top_left, Button_colour, Text, Font):
        self.screen = Screen
        self.rect = pygame.Rect((Top_left), (Width,Height) )
        self.width = Width
        self.height = Height
        self.button_colour = Button_colour
        self.text = Text
        self.font = Font

    def draw(self):
        pygame.draw.rect(self.screen, self.button_colour, self.rect, 1)
        self.write_text()
        
    def write_text(self): 
        text_length = self.font.size(self.text)[0]
        x_padding = (self.width - text_length) / 2
        text_height = self.font.size(self.text)[1]
        y_padding = (self.height - text_height) / 2

        self.screen.blit(self.font.render(self.text, True, (0,0,0)),(self.rect.topleft[0]+x_padding,self.rect.topleft[1]+y_padding))
        
    def detect_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
            else:
                return False
            
        
        
