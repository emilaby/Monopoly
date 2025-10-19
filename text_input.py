import pygame

from constants import *

class Text_input:
    """
    This class handles rendering an interactive text box, capturing user input,
    and updating the displayed text.
    """
    def __init__(self, Top_left, Width, Height, Screen):
        self.top_left = Top_left
        self.width = Width
        self.height = Height
        self.screen = Screen
        self.inactive_colour = textbox_inactive_colour #colour of box when it hasn't been pressed/isn't being used
        self.active_colour = textbox_active_colour #colour of box when in use
        self.current_colour = self.inactive_colour #starts off inactive
        self.text = ''
        self.rect = pygame.Rect(Top_left, (Width,Height))
        self.active = False
        self.font = pygame.font.SysFont('timesnewroman',20)
        self.text_surface = self.font.render(self.text,True,text_colour)
    
    def draw(self):
        pygame.draw.rect(self.screen, self.current_colour, self.rect, 1)
        self.screen.blit(self.text_surface,(self.top_left))
    
    #detects text entered
    def text_entered(self, event):
        mouse_pos = pygame.mouse.get_pos() #stores position of mouse
        mouse_pressed = pygame.mouse.get_pressed()[0] #if True, this means left click
        if mouse_pressed == True:
            if self.rect.collidepoint(mouse_pos): #checks whether position of mouse within box 
                self.active = True #if button is pressed, it becomes active 
                self.current_colour = self.active_colour
            else:
                self.active = False
                self.current_colour = self.inactive_colour
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key in [pygame.K_TAB,pygame.K_ESCAPE]:
                    pass
                elif self.font.size(self.text+event.unicode)[0] <= self.width:
                        self.text += event.unicode
                self.text_surface = self.font.render(self.text,True,text_colour)
        else:
            return False

