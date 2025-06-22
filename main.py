from config import *
import sys
import game_over as gg
import setting_class as Settings
import card_class as Card

#Get initial position 
def get_card_center():
  x_pos = WIDTH//2 -CARD_WIDTH//2 
  y_pos = HEIGHT//2 - CARD_HEIGHT//2
  return x_pos, y_pos
#############

def draw_window():
  #WINDOW.fill("white")
  #pygame.draw.circle(WINDOW, 'red', (30,30), 10, 0)
  WINDOW.blit(BACKGROUND, (0,0))
  x_pos,y_pos = get_card_center()
  WINDOW.blit(CARD_BACK, (x_pos, y_pos))
  WINDOW.blit(CARD_BACK, (x_pos - CARD_WIDTH - X_SPACING, y_pos))
  WINDOW.blit(CARD_BACK, (x_pos + CARD_WIDTH + X_SPACING, y_pos))
  # Create rects for collision detection
  cards_hit_boxes =[]
  cards_hit_boxes.append(CARD_BACK.get_rect(topleft=(x_pos - CARD_WIDTH - X_SPACING, y_pos)))
  cards_hit_boxes.append(CARD_BACK.get_rect(topleft=(x_pos, y_pos)))
  cards_hit_boxes.append(CARD_BACK.get_rect(topleft=(x_pos + CARD_WIDTH + X_SPACING, y_pos)))
  #card_one_rect   = CARD_BACK.get_rect(topleft=(x_pos - CARD_WIDTH - X_SPACING, y_pos))
  #card_two_rect   = CARD_BACK.get_rect(topleft=(x_pos, y_pos))
  #card_three_rect = CARD_BACK.get_rect(topleft=(x_pos + CARD_WIDTH + X_SPACING, y_pos))
  pygame.display.update()
  return cards_hit_boxes

'''
Take the selected choice from player as parameter,
draw the corresponding cards
'''
def draw_show_down(selected_pos):
  x_pos, y_pos = get_card_center()
  WINDOW.blit(QUEEN, (x_pos,y_pos))
  WINDOW.blit(ACE, (x_pos - (CARD_WIDTH + X_SPACING),y_pos))
  WINDOW.blit(ACE, (x_pos + (CARD_WIDTH + X_SPACING),y_pos))
  pygame.display.update()
  return

def get_selected_card(mouse_pos, cards_hit_box):
  for i, hit_box in enumerate(cards_hit_box): 
    if hit_box.collidepoint(mouse_pos):
      print(f"Card {i+1} clicked")
      draw_show_down(mouse_pos)
  return i

class Game:
  def __init__(self):
    pygame.init()
    self.clock = pygame.time.Clock()
    #set the tick (fps) in main loop
    self.settings = Settings.Settings()
    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Monte Carlo")
    #Draw background 
    self.game_active = True #Control game start or not 
    #Create cards sprite group 
    self.down_cards = pygame.sprite.Group()
  '''
  To update screen 
  '''
  def _update_screen(self):
    self.screen.blit(self.settings.background, (0,0)) #Draw game background
    self._create_three_cards()
    self.down_cards.draw(self.screen)
    pygame.display.update()

  #main game loop
  def game_loop(self):
    running = True 
    while self.game_active: 
      self.clock.tick(60)
      self._update_screen() 
      self._check_events()
    print("out of loop")
    pygame.quit()
    sys.exit()

  def _check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.game_active = False
      '''
      if event.type == pygame.MOUSEBUTTONDOWN:
        if self.game_active:
          mouse_pos = pygame.mouse.get_pos()
          get_selected_card(mouse_pos, cards_hit_box)        
          #change game-state
          self.game_active = False
          pygame.time.delay(1000)
        else:
          cards_hit_box= []
          cards_hit_box = gg.play_again()
          mouse_pos = pygame.mouse.get_pos()
          for i, hit_box in enumerate(cards_hit_box): 
            if hit_box.collidepoint(mouse_pos):
              print(f"Option {i+1} clicked")
      '''
  def _create_three_cards(self):
    card = Card.Card(self)  
    width,height = card.rect.size
    #print(width) #81 expect?
    current_centerx = card.rect.centerx
    current_centery = card.rect.centery - 100
    self._create_card(current_centerx, current_centery)
    self._create_card(current_centerx - (width+20), current_centery)
    self._create_card(current_centerx + (width+20), current_centery)

  def _create_card(self, x_pos, y_pos):
    new_card = Card.Card(self)
    new_card.rect.centerx = x_pos 
    new_card.rect.centery = y_pos 
    self.down_cards.add(new_card)

def main():
  game = Game()
  game.game_loop()
  return 
    
if __name__ == '__main__':
  main()