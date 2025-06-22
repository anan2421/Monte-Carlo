from setting_class import *
from pygame.sprite import Sprite

class Card(Sprite):
  def __init__(self, game):
    super().__init__()
    self.screen = game.screen #constructor for game window
    self.settings = game.settings
    self.face_down = True #Card face-down
    self.card_back = self.settings.card_back
    self.queen_of_heart = self.settings.card_queen
    self.ace_of_heart = self.settings.card_ace

    #self.card_rect = self.card_back.get_rect()
    #self.card_rect.centerx = self.settings.width/2
    #self.card_rect.centery = self.settings.height/2

    # Start with face-down image
    self.image = self.card_back
    self.rect = self.image.get_rect()

    # Position at center of screen
    self.rect.centerx = self.settings.screen_width / 2
    self.rect.centery = self.settings.screen_height / 2

