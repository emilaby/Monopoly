import random
import pygame

class Dice:
    """
    This class handles rolling the dice, selecting the correct dice face image
    based on the roll, and displaying the dice image on the game screen.
    """
    def __init__(self, Screen, Topleft):
        self.current_num = None
        self.current_image = None
        self.screen = Screen
        self.topleft = Topleft

    def roll(self):
        self.current_num = self.generate_num()
        self.dice_image(self.current_num)
        self.draw_img()
    
    def generate_num(self): #generates a random number between 1 and 6 inclusive
        return random.randint(1,6)



    def dice_image(self, num): #selects which dice face to display based on the number rolled
        if num == 1:
            self.current_image = "dice1.png"
        elif num == 2:
            self.current_image = "dice2.png"
        elif num == 3:
            self.current_image = "dice3.png"
        elif num == 4:
            self.current_image = "dice4.png"
        elif num == 5:
            self.current_image = "dice5.png"
        elif num == 6:
            self.current_image = "dice6.png"
        
    def draw_img(self): #blits the correct dice image to the screen
        image = pygame.image.load(self.current_image)
        self.screen.blit(image,self.topleft)
    


