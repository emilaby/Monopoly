import pygame
from constants import *

class Board:
    """
    This class is responsible for rendering the entire Monopoly board using Pygame,
    including the four sides of tiles and the "MONOPOLY" text in the centre.
    It also handles splitting long tile names into multiple lines so that text fits
    within each tile.    
    """
    def __init__(self,Screen,Tile_names):
        self.screen = Screen
        self.counter = -1
        self.font = tile_font
        self.tile_names = Tile_names
    
    def draw_tiles(self):
        text_length = monopoly_text_font.size('MONOPOLY')[0]
        text_height = monopoly_text_font.size('MONOPOLY')[1]
        
        text_topleftx = (490-text_length)/2 + 107
        text_toplefty = (490-text_height)/2 + 107
        self.screen.blit(monopoly_text_font.render('MONOPOLY', True, (0,0,0)),(text_topleftx,text_toplefty))
        
        self.draw_top_tiles()
        self.draw_right_tiles()
        self.draw_bottom_tiles()
        self.draw_left_tiles()


    def line_of_text(self,text,width): #returns substring that fits within given width
        current_string = ''
        i = 0
        while self.font.size(current_string)[0] < width-2 and i < len(text): #width-2 to provide adequate spacing between 
                                                                             #tiles and to account for the padding on the left hand side of the tile
            current_string += text[i]
            i += 1
        return current_string[0:-1], i-1 #when while loop ends, text will have too big a width 
                                            #so we want the string from the previous iteration of the while loop
    
    def multiline_text(self,string,rectangle,width): #splits string into lines of length, width input
        text = self.font.render(string, True, (0,0,0))
        text_length = self.font.size(string)[0]
        text_height = self.font.size(string)[1]
        if text_length > width-4: #width-4 to provide spacing, so text from neighboring tiles does not touch
            #2 lines below split the string into 2 lines of text
            string1,i = self.line_of_text(string,width) 
            string2 = string[i::] #string2 is the remaining text from string variable
            #blit string1 and string2 separately, 2 below 1
            text = self.font.render(string1,True,(0,0,0))
            coord1 = (rectangle.topleft[0]+2,rectangle.topleft[1]) #+2 to the x coordinate so there is spacing between text of different tiles
            self.screen.blit(text,coord1)
            text = self.font.render(string2,True,(0,0,0))
            coord2 = (rectangle.topleft[0]+2,rectangle.topleft[1]+text_height)
            self.screen.blit(text,coord2)
        else:
            coord1 = (rectangle.topleft[0]+2,rectangle.topleft[1])
            self.screen.blit(text, coord1)
 
    def draw_top_tiles(self):
        self.counter += 1
        rectangle = pygame.draw.rect(self.screen, tile_colour, (0,0,square_w,square_h),1)#topleft
        string = self.tile_names[self.counter] #stores the full name of the tile
        self.multiline_text(string,rectangle,square_w)
    
        for i in range (7):
            self.counter+=1
            rectangle = pygame.draw.rect(self.screen, tile_colour, ((square_w+(rect_w*i)),0,rect_w,rect_h),1)
            string = self.tile_names[self.counter]
            self.multiline_text(string,rectangle,rect_w)
            
        self.counter += 1
        rectangle = pygame.draw.rect(self.screen, tile_colour, ((board_w-square_w),0,square_w,square_h),1)#topright
        string = self.tile_names[self.counter]
        self.multiline_text(string,rectangle,square_w)

    def draw_bottom_tiles(self):
        self.counter += 1
        rectangle = pygame.draw.rect(self.screen, tile_colour, ((board_w - square_w),(board_h - square_h),square_w,square_h),1) #bottomright
        string = self.tile_names[self.counter]
        self.multiline_text(string,rectangle,square_w)
        
        #bottom right rect: topleftx coordinate of square_w + 6*rect_w
        #each successive rectangle, subtract rect_w from topleftx

        for i in range (7):
            self.counter += 1
            rectangle = pygame.draw.rect(self.screen, tile_colour, ((square_w+(rect_w*6)-(rect_w*i)),(board_h - square_h),rect_w,rect_h),1)
            string = self.tile_names[self.counter]
            self.multiline_text(string,rectangle,rect_w)

        self.counter += 1
        rectangle = pygame.draw.rect(self.screen, tile_colour, (0,(board_h - square_h),square_w,square_h),1) #bottomleft
        string = self.tile_names[self.counter]
        self.multiline_text(string,rectangle,square_w)

    def draw_left_tiles(self):
        
        #bottom left rect: toplefty coordinate of square_w + 6*rect_w
        #each successive rectangle, subtract rect_w from y
        
        for i in range(7):
            self.counter += 1
            rectangle = pygame.draw.rect(self.screen, tile_colour, (0, (square_w+(6*rect_w)-(i*rect_w)), rect_h, rect_w), 1)
            string = self.tile_names[self.counter]
            self.multiline_text(string,rectangle,rect_h) #horizontal tile so rather than rect_w, width parameter is rect_h

    def draw_right_tiles(self):
        for i in range(7):
            self.counter += 1
            rectangle = pygame.draw.rect(self.screen, tile_colour, ((board_w - square_w), (square_w+(rect_w*i)), rect_h, rect_w), 1)
            string = self.tile_names[self.counter]
            self.multiline_text(string,rectangle,rect_h)





            