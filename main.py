import pygame
import sys

pygame.init()

#File imports
from constants import *
from token_sprite import Token
from board import Board
from dice import Dice
from property import Property
from board import Board
from button import Button
from load_board_data import tile_names, tile_object_names, tile_types, tile_prices
from text_input import Text_input
from find_obj import find_obj

#Screen initialisation
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Monopoly")
screen.fill(screen_colour)

clock = pygame.time.Clock()

#Dice objects
dice1 = Dice(screen,(910,617))
dice2 = Dice(screen,(990,617))

#Token button objects
tophat_button = Button(screen, 250,100, (325,250),(0,0,0), 'Tophat', num_button_font)
shoe_button = Button(screen, 250,100, (725,250),(0,0,0), 'Shoe',num_button_font)
racing_car_button = Button(screen, 250,100, (325,400),(0,0,0), 'Racing car',num_button_font)
dog_button = Button(screen, 250,100, (725,400),(0,0,0), 'Dog',num_button_font)
iron_button = Button(screen, 250,100, (525,550),(0,0,0), 'Iron',num_button_font)


token_buttons = [tophat_button, shoe_button, racing_car_button, dog_button, iron_button]

#Token objects
top_hat = Token("tophat","tophat.png")
shoe = Token("shoe","shoe.png")
racing_car = Token("racingcar","racingcar.png")
dog = Token("dog","dog.png")
iron = Token("iron","iron.png")


token_group = pygame.sprite.Group()

token_button_class_dict = {tophat_button:top_hat,
                           shoe_button:shoe,
                           racing_car_button:racing_car,
                           dog_button:dog,
                           iron_button:iron} #stores the link between token buttons and their class objects

#Button objects
start_game_button = Button(screen, 350, 100, (465,375), (0,0,0), 'Start Game',num_button_font)
two_button = Button(screen, 100,100, (340,400),(0,0,0), '2',num_button_font)
three_button = Button(screen, 100,100, (506,400),(0,0,0), '3',num_button_font)
four_button = Button(screen, 100,100, (673,400),(0,0,0), '4',num_button_font)
five_button = Button(screen, 100,100, (840,400),(0,0,0), '5',num_button_font)

enter_button = Button(screen, 250,100, (1010,600),(0,0,0), 'Enter',num_button_font)

dice_roll_button = Button(screen, 150, 100, (750,602), (0,0,0), 'Roll dice',num_button_font)

yes_button = Button(screen, 75, 60, (823,460), (0,0,0), 'Yes', yes_no_button_font)
no_button = Button(screen, 75, 60, (939,460), (0,0,0), 'No', yes_no_button_font)

quit_button = Button(screen, 75, 60, (575,310), (0,0,0), 'Quit', yes_no_button_font)
bid_input = Text_input((260,290),300,100,screen)

continue_button = Button(screen, 250, 75, (1020,630), (0,0,0), 'Continue', num_button_font)


#Text_input objects
name_boxes=[]

name_box1 = Text_input((275,250),350,100,screen)
name_box2 = Text_input((675,250),350,100,screen)
name_box3 = Text_input((275,400),350,100,screen)
name_box4 = Text_input((675,400),350,100,screen)
name_box5 = Text_input((475,550),350,100,screen)

name_boxes.append(name_box1)
name_boxes.append(name_box2)
name_boxes.append(name_box3)
name_boxes.append(name_box4)
name_boxes.append(name_box5)


#Property objects
property_objects = []
for each in tile_object_names:
    if tile_types[tile_object_names.index(each)] in ['Property', 'Station', 'Utility']: #checks if the tile is of the correct type
        name = tile_names[tile_object_names.index(each)]
        exec(each+' = Property(name)')
        exec('property_objects.append('+each+')')

#Other variables 
i = 0
game_started = False
display_purchase_rect = False
player_token_dict = {} #stores the player name:token class for that player's selected token
last_moved = ''
player_i = 0 #index of current player
moved = False
info = []
number_of_players = ''
count = 0
player_names = []
names_submitted = False
condition = True   
current_screen = 'menu'
info_max_size = 10


#Game loop
while condition:        
    for event in pygame.event.get():
        next_event = False

        if event.type == pygame.QUIT:
            condition = False
            pygame.quit()
            sys.exit()
        #Menu
        if current_screen == 'menu':
            screen.fill(screen_colour)
            screen.blit(pygame.font.SysFont('arialblack',65).render("Monopoly",True,(0,0,0)),(465,100))
            start_game_button.draw()

        #Start game pressed   
        if start_game_button.detect_click(event) and current_screen == 'menu':
            next_event = True
            current_screen = 'num of players'
            screen.fill(screen_colour)
            screen.blit(pygame.font.SysFont('arialblack',40).render("Select number of players:",True,(0,0,0)),(360,100))
            two_button.draw()
            three_button.draw()
            four_button.draw()
            five_button.draw() 
        
        #Select number of players
        if current_screen == 'num of players' and not next_event:
            if two_button.detect_click(event):
                number_of_players = 2
            elif three_button.detect_click(event):
                number_of_players = 3
            elif four_button.detect_click(event):
                number_of_players = 4
            elif five_button.detect_click(event):
                number_of_players = 5
            
            if number_of_players != '':
                current_screen = 'player names'
                screen.fill(screen_colour)
                screen.blit(pygame.font.SysFont('arialblack',40).render("Enter player names:",True,(0,0,0)),(425,100))
                enter_button.draw()

        #Enter player names   
        if current_screen == 'player names':
            name_boxes = name_boxes[0:number_of_players]
            if enter_button.detect_click(event):
                names_entered = True
                for each in name_boxes:
                    if each.text == '':
                        names_entered = False
                if names_entered:    
                    names_submitted = True
                
            for box in name_boxes:
                box.text_entered(event)
                pygame.draw.rect(screen, screen_colour, box.rect) #draws a rectangle over the textbox so it can be drawn again
                box.draw()

            if names_submitted:
                current_screen = 'token selection'
                screen.fill(screen_colour)
                player_names = []
                for box in name_boxes:
                    player_names.append(box.text) #stores a list of sumbitted player names
                
                for player in player_names:
                    #adds players to player_token_dict 
                    player_token_dict[player] = ''
                    
        #Token selection        
        if current_screen == 'token selection':
            current_selecting_player = player_names[i]
            screen.fill(screen_colour)
            screen.blit(pygame.font.SysFont('arialblack',40).render("Select your token "+str(current_selecting_player),True,(0,0,0)),(425,100))
            for each in token_buttons:
                each.draw()
                if each.detect_click(event):
                    i+=1
                    token_buttons.remove(each)
                    player_token_dict[current_selecting_player] = token_button_class_dict[each]
                    token_group.add(token_button_class_dict[each])
                    token_button_class_dict[each].player_name = current_selecting_player #adds the required token class objects to the token_group 
                    
            if i > len(player_names)-1:
                for each in token_group:
                    if number_of_players == 2:
                        each.money = 900
                    elif number_of_players == 3:
                        each.money = 700
                    elif number_of_players == 4:
                        each.money = 600
                    elif number_of_players == 5:
                        each.money = 300
                    
                #Tutorial screen
                current_screen = 'tutorial'
                screen.fill(screen_colour)
                text_length = pygame.font.SysFont('arialblack',50).size('Tutorial')[0]
                tutorial_heading_topleftx = (1280 - text_length) / 2

                screen.blit(pygame.font.SysFont('arialblack',50).render('Tutorial',True,(0,0,0)),(tutorial_heading_topleftx,10))
                tutorial_text_i = 0
                for each in tutorial_text:
                    if each != '':
                        text_length = body_font.size(each)[0]
                        text_height = body_font.size(each)[1]
                        tutorial_text_topleftx = (1280 - text_length) / 2
                        tutorial_text_toplefty = (tutorial_text_i* 40) + 100
                        screen.blit(body_font.render(each, True, (0,0,0)),(tutorial_text_topleftx,tutorial_text_toplefty))
                        tutorial_text_i += 1
                    else:
                        tutorial_text_i += 1

                continue_button.draw()
                
        if current_screen == 'tutorial':
            if continue_button.detect_click(event):
                current_screen = 'main game'
            

        #Main game screen
        if current_screen == 'main game':
            player_i = player_i % number_of_players #mod used so index doesn't go out of range
            current_player = player_names[player_i]
            current_player_token = player_token_dict[current_player]
            
            screen.fill(screen_colour)
            
            #Current player name 
            current_player_text_surface = med_bold_font.render('Current player: '+current_player, True, (0,0,0))
            screen.blit(current_player_text_surface, (755, 575))

            board = Board(screen,tile_names)
            board.draw_tiles() 
            token_group.draw(screen) #draws the tokens added to token_group

            #Jail
            if current_player_token.in_jail:
                current_player_token.move_to_jail()
                
                screen.fill(screen_colour)
                screen.blit(current_player_text_surface, (755, 575))
                board = Board(screen,tile_names)
                board.draw_tiles() 
                token_group.draw(screen)

                if current_player_token.money < 50:
                    player_names.remove(current_player)
                    number_of_players = len(player_names) #prevents list index out of range error
                    token_group.remove(player_token_dict[current_player])
                    info.append(current_player+' unable to pay jail fine so is out')
                    player_i += 1
                    moved = False
                else:
                    current_player_token.money -= 50
                    info.append(current_player+' paid 50 to leave jail')
                    current_player_token.in_jail = False
                
            #Stats
            for player in player_names: 
                ind = player_names.index(player)
                money = player_token_dict[player].money
                stat_name_text_surface = body_font.render(player, True, (0,0,0))
                stat_money_text_surface = body_font.render(str(money), True, (0,0,0))
                
                screen.blit(stat_name_text_surface, (1120,60+ind*55))
                screen.blit(stat_money_text_surface, (1214,60+ind*55))
                
            stat_name_heading = title_med_font.render('Player:', True, (0,0,0))
            stat_money_heading = title_med_font.render('Money:', True, (0,0,0))
        
            screen.blit(stat_name_heading, (1100,15))
            screen.blit(stat_money_heading, (1200,15))
            
            pygame.draw.rect(screen, (0,0,0), (1090,15, 180,300), 1)
            pygame.draw.rect(screen, (0,0,0), (1090,15, 180,35), 1)
            
            dice_roll_button.draw()
            
            #Dice roll detection
            if dice_roll_button.detect_click(event) and last_moved != current_player:
                game_started = True
                dice1.roll()
                dice2.roll()
                spaces_to_move = dice1.current_num + dice2.current_num
                current_player_token.move(spaces_to_move)
                
                moved = True
                last_moved = current_player
                

                    
                #GO tile
                if 'GO' in tile_names[current_player_token.current_position-spaces_to_move+1:current_player_token.current_position+1]:
                    current_player_token.money += 50
                    info.append('50 credited to '+current_player+' for landing on/passing GO')
                
                #Tax tile
                if tile_types[current_player_token.current_position] == 'Tax':
                    current_player_token.money -= tile_prices[current_player_token.current_position]
                    info.append(tile_names[current_player_token.current_position]+' of '+str(tile_prices[current_player_token.current_position])+' deducted from '+current_player)
                    if current_player_token.money < 0:
                        player_names.remove(current_player)
                        number_of_players = len(player_names) #prevents list index out of range error
                        token_group.remove(player_token_dict[current_player])
                        info.append(current_player+' bankrupt')
            #Jail             
            if moved and tile_names[current_player_token.current_position] == 'GO TO JAIL':
                current_player_token.in_jail = True
                info.append(current_player+' is in jail')
                
                        
            #Doubles         
            if not current_player_token.in_jail and moved and dice1.current_num == dice2.current_num:
                moved = False #stops rest of if statements running
                last_moved = player_names[player_i - 1] 
                info.append(current_player+' rolled doubles')
        
            #Purchase property
            if  moved and tile_types[current_player_token.current_position] in ['Property', 'Station', 'Utility'] and (find_obj(tile_names[current_player_token.current_position],property_objects)).owner == None and (find_obj(tile_names[current_player_token.current_position],property_objects)).get_price() <= current_player_token.money:
                #option to purchase/charge them rent
                purchase_rect = pygame.Rect((720,370),(397,200))
                pygame.draw.rect(screen, (0,0,0) ,purchase_rect , 1)
                current_property_object = find_obj(tile_names[current_player_token.current_position],property_objects)

                text1 = 'Would you like to purchase ' + tile_names[current_player_token.current_position] + '?'
                text2 = 'Price: '+ str(current_property_object.get_price())
                screen.blit(med_bold_font.render(text1, True, (0,0,0)), (723,375))
                screen.blit(body_font.render(text2, True, (0,0,0)), (724,403))
                yes_button.draw()
                no_button.draw()
                if yes_button.detect_click(event):
                    player_i += 1
                    moved = False
                    current_player_token.add_property(current_property_object) #adds property object to properties array
                    current_property_object.owner = current_player_token    
                    current_player_token.money -= current_property_object.get_price()
                elif no_button.detect_click(event):
                    player_i += 1
                    moved = False

            #Charge rent        
            elif  moved and tile_types[current_player_token.current_position] in ['Property', 'Station', 'Utility'] and (find_obj(tile_names[current_player_token.current_position],property_objects)).owner not in [None, player_token_dict[current_player]]:
                current_property_object = find_obj(tile_names[current_player_token.current_position],property_objects)
                current_player_token.money -= current_property_object.get_rent()
                info.append(current_player+' landed on '+current_property_object.owner.player_name+"'s property. Rent deducted = "+ str(current_property_object.get_rent()))
                if current_player_token.money < 0:
                    player_names.remove(current_player)
                    token_group.remove(player_token_dict[current_player])
                    number_of_players = len(player_names) #prevents list index out of range error
                    info.append(current_player+' bankrupt')
                    
                current_property_object.owner.money += current_property_object.get_rent()
                player_i += 1
                moved = False
                
            elif not current_player_token.in_jail and moved:
                player_i += 1
                moved = False
            
                                            
            if game_started:
                dice1.draw_img()
                dice2.draw_img()
            
            #Display player name near token
            for player in player_names:
                token_rect = player_token_dict[player].rect
                x = token_rect.centerx
                y = token_rect.centery
                if player_token_dict[player].name == 'dog':
                    x += 20
                    y += 12
                elif player_token_dict[player].name == 'iron':
                    y += 15
                elif player_token_dict[player].name == 'racingcar':
                    y += 7
                elif player_token_dict[player].name == 'tophat':
                    y += 15
                    x -= 3
                elif player_token_dict[player].name == 'shoe':
                    y += 15
                
                player_name_text_surface = small_font.render(player, True, (0,0,0))
                screen.blit(player_name_text_surface, (x, y))
                token_group.draw(screen)
            
            #info box (displays most recent 9 lines of text stored)
            pygame.draw.rect(screen, (0,0,0), ((720,10), (360, 350)),1)

            text_surface = title_med_font.render('Information:', True, (0,0,0))
            screen.blit(text_surface, (850, 15))
            if len(info) > 0:
                if len(info) >= 10:
                    info = info[-9:]
                    ind = 0
                    for each in info:
                        text_surface = very_small_font.render(info[ind], True, (0,0,0))
                        screen.blit(text_surface, (723, 40+ind*35))
                        ind += 1
                else:
                    ind = 0
                    for each in info:
                        text_surface = very_small_font.render(info[ind], True, (0,0,0))
                        screen.blit(text_surface, (723, 40+ind*35))
                        ind+=1
            if number_of_players == 1:
                current_screen = 'game over'
        
        #Game over
        if current_screen == 'game over':
            screen.fill(screen_colour)
            text = player_names[0]+' wins'
            text_length = large_heading_font.size(text)[0]
            text_height = large_heading_font.size(text)[1]
            x = (1280 - text_length) / 2
            y = (720 - text_height) / 2
            screen.blit(large_heading_font.render(text, True, (0,0,0)), (x, y))
        
    pygame.display.flip()

    clock.tick(60)
    
    

        
