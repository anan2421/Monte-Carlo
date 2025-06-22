from config import *

'''
A class to store all settings
'''
class Settings():
  def __init__(self):
    #Screen settings
    self.screen_width = 1280
    self.screen_height = int(self.screen_width*(9/16)) 
    #Card 
    self.card_height = int(self.screen_height/2)
    self.card_width = int(self.card_height * (9/16))
    #Card Designs
    #Back design
    self.card_back = pygame.image.load(os.path.join('Assets', 'card_back.png'))
    self.card_back = pygame.transform.scale(self.card_back, (self.card_width, self.card_height))
    #Face up design
    self.card_queen = pygame.image.load(os.path.join('Assets', 'queen_of_hearts.png'))
    self.card_queen = pygame.transform.scale(self.card_queen, (self.card_width, self.card_height))
    self.card_ace = pygame.image.load(os.path.join('Assets', 'ace_of_hearts.png'))
    self.card_ace = pygame.transform.scale(self.card_ace, (self.card_width, self.card_height))
    
    #Background
    self.background = pygame.image.load(os.path.join('Assets', 'background.png'))
    self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))
    #Add more settings if needed
    