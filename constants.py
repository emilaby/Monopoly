import pygame

screen_colour = pygame.Color(191, 219, 174)
tile_colour = pygame.Color(0,0,0)
textbox_inactive_colour = pygame.Color(0, 0, 0)
textbox_active_colour = pygame.Color(255, 255, 255)
text_colour = pygame.Color(0, 0, 0)
square_w = 107
square_h = 107

rect_w = 70
rect_h = 107
board_w = 2*square_w + 7*rect_w
board_h = 2*square_w + 7*rect_w

tile_font = pygame.font.SysFont('arialblack',12)
monopoly_text_font = pygame.font.SysFont('arialblack',70)

body_font = pygame.font.SysFont('timesnewroman',18)
heading_font = pygame.font.SysFont('timesnewroman',23)
large_heading_font = pygame.font.SysFont('arialblack',60)
num_button_font = pygame.font.SysFont('arialblack',20)
yes_no_button_font = pygame.font.SysFont('arialblack',18)
auction_heading_font = pygame.font.SysFont('arialblack',23)
auction_body_font = pygame.font.SysFont('timesnewroman',22)
small_font = pygame.font.SysFont('timesnewroman',19)
very_small_font = pygame.font.SysFont('timesnewroman',17)
med_bold_font = pygame.font.SysFont('arialblack',15)
title_med_font = pygame.font.SysFont('arialblack',17)

tile_center_x = [square_w/2, square_w + rect_w/2]
tile_center_y = [square_w/2]

# TOP ROW
for i in range (6):
    tile_center_x.append(tile_center_x[-1] + rect_w) #moving between rectangles
for i in range (8):
    tile_center_y.append(tile_center_y[0]) #rest of row
tile_center_x.append(tile_center_x[-1] + rect_w/2+square_w/2) #top right

# RHS COL
for i in range (8): 
    tile_center_x.append(tile_center_x[-1]) #rest of col
tile_center_y.append(tile_center_y[-1]+square_w/2 + rect_w/2) #first rectangle in rhs col
for i in range (6): 
    tile_center_y.append(tile_center_y[-1] + rect_w) #moving between rectangles
tile_center_y.append(tile_center_y[-1]+rect_w/2 + square_w/2) #bottom right

# BOTTOM ROW
tile_center_x.append(tile_center_x[-1]-square_w/2-rect_w/2) #first rectangle in bottom row
for i in range (6):
    tile_center_x.append(tile_center_x[-1]-rect_w) #moving between rectangles
for i in range (8):
    tile_center_y.append(tile_center_y[-1]) #rest of row
tile_center_x.append(tile_center_x[-1]-rect_w/2-square_w/2) #bottom left

# LHS COL
for i in range (7):
    tile_center_x.append(tile_center_x[-1]) #rest of col
tile_center_y.append(tile_center_y[-1]-square_w/2 - rect_w/2) #first rectangle in col

for i in range (6):
    tile_center_y.append(tile_center_y[-1]-rect_w) #moving between rectangles


tutorial_text = ['On your turn, press the roll dice button which rolls two dice and your token will move that many ',
                 'spaces on the board.',
                 '',
                 'When landing on properties, railroads or utilities that are unowned, you can purchase them. If ',
                 'they are owned by another player, you will be charged rent.',
                 '',
                 'When landing on tax spaces, you will be charged a fee.',
                 '',
                 'If you land on the "GO TO JAIL" tile, you will be sent to jail. 50 will be charged to escape jail, which',
                 'if causes you to become bankrupt will result in removal from the game. ',
                 '',
                 '50 is credited when you pass or land on the "GO" tile.',
                 '',
                 'The game continues until all players except one is bankrupt, this player is the winner.']




