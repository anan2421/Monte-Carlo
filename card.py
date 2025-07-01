from setting_class import *
from pygame.sprite import Sprite
import random 

class Card(Sprite):
  def __init__(self, game):
    super().__init__()
    self.screen = game.screen #constructor for game window
    self.settings = game.settings
    self.face_down = True #Card face-down
    self.card_back = self.settings.card_back
    self.queen_of_heart = self.settings.card_queen
    self.ace_of_heart = self.settings.card_ace

    # Start with face-down image
    self.image = self.card_back
    self.rect = self.image.get_rect()

    # Position at center of screen
    self.rect.centerx = self.settings.screen_width / 2
    self.rect.centery = self.settings.screen_height / 2

  # Return True to let user win 
  def __gamble__(self) -> True:
    numb_one = random.randint(1,1)
    numb_two = random.randint(1, 3)
    if numb_one == numb_two:
      return True
    return False

  def _create_card(self, x_pos, y_pos):
    new_card = Card(self)
    new_card.rect.centerx = x_pos 
    new_card.rect.centery = y_pos 
    #self.down_cards.add(new_card)
    return new_card

  def blit_card(self):
    self.screen.blit(self.image, self.rect)

  # update card design
  def update_card(self, index= None):
    match index: 
      case 1: 
        self.image = self.queen_of_heart
      case 2:
        self.image = self.ace_of_heart
      case _:
        self.image = self.card_back

class Cards(Card): 
  # Since the cards position are fixed
  def __init__(self, game):
    super().__init__(game)
    #self.cards = pygame.sprite.Group()
    self.cards = []
    self._create_three_cards()

  def _create_three_cards(self):
    card = Card(self)  
    width,height = card.rect.size
    #print(width) #81 expect?
    current_centerx = card.rect.centerx
    current_centery = card.rect.centery - 100
    for i in range(3):
      pass
    self.cards.append(self._create_card(current_centerx - (width+20), current_centery))
    self.cards.append(self._create_card(current_centerx, current_centery))
    self.cards.append(self._create_card(current_centerx + (width+20), current_centery))
  
  def _draw_card(self):
    for card in self.cards:
      #self.cards.draw(self.screen)
      card.blit_card()

  def _flip_cards(self, choice: int =0):
    win = self.__gamble__()
    if win:
      print(f"win")
      for i, card in enumerate(self.cards):
        if i != choice: 
          #print(f"i not choice {i} vs {choice}")
          card.update_card(2)
        else: 
          #print(f"i is choice {i} vs {choice}")
          card.update_card(1)
    else: 
      print(f"Lose")
      queen_flipped = False
      loop_count = 0
      #self.cards[choice].update_card(2)
      queen_choice = 0
      for i, card in enumerate(self.cards):
        if i == choice: 
          card.update_card(2)
        else: 
          if loop_count < 1:
            queen_choice = random.choice([1,2])  
            card.update_card(queen_choice)
            loop_count += 1
            #if queen_choice < 2:
            #  queen_choice += 1
          else:
            card.update_card((queen_choice)%2 + 1)
    self._draw_card()
    return win
  
  def _reset_cards(self):
    for card in self.cards: 
      card.update_card(0)
  
  def _get_selected_card(self, mouse_pos) -> int:
    #choice = -1
    for i, hit_box in enumerate(self.cards):
      if hit_box.rect.collidepoint(mouse_pos):
        #print(f"Card {i+1} clicked")
        return i
    return None

  