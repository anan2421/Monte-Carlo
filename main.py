from config import *
import sys
import game_over as gg
from setting_class import Settings
import card 
RESET_CARD_EVENT = pygame.USEREVENT + 1
#pygame.event.post(pygame.event.Event(RESET_CARD_EVENT))
class Button(): 
  def __init__(self, settings, text, x, y, width=200, height=50, font_size=36):
    self.settings = settings  # Assume this holds shared styles or colors
    self.screen = settings.screen
    self.text = text
    self.rect = pygame.Rect(x, y, width, height)
    self.font = pygame.font.SysFont(None, font_size)

    # Colors from settings or defaults
    self.button_color = getattr(settings, "button_color", (0, 128, 0))  # Dark green
    self.text_color = getattr(settings, "text_color", (255, 255, 255))  # White

    self.text_image = self.font.render(self.text, True, self.text_color)
    self.text_rect = self.text_image.get_rect(center=self.rect.center)

  def draw(self):
    pygame.draw.rect(self.screen, self.button_color, self.rect)
    self.screen.blit(self.text_image, self.text_rect)
  
  def move(self):
    velocity = 1
    
    self.rect.centerx += 1
    self.rect.centery += 1
    self.text_rect.center = self.rect.center  # ← keep text centered
    #self.draw()
  
class Game:
  def __init__(self):
    pygame.init()
    self.clock = pygame.time.Clock()
    #set the tick (fps) in main loop
    self.settings = Settings()
    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Monte Carlo")
    #Mouse clicked
    self.mouse_clicked = False
    self.cards_up = False
    #Draw background 
    self.game_active = True #Control game start or not 
    #Create 3 cards
    self.cards = card.Cards(self)
    #-----
    self.win_button = [] #Button(self, "You Win", 720, 360)
    self.win_or_lose = False
  '''
  To update screen 
  '''
  def _update_screen(self):
    self.screen.blit(self.settings.background, (0,0)) #Draw game background
    #self.cards.blit_card()
    self.cards._draw_card()
    for button in self.win_button:
      #self.win_button.move()
      #self.win_button.draw()
      button.move()
      button.draw()
    #pygame.display.update()

  #main game loop
  def game_loop(self):
    running = True 
    while self.game_active: 
      self.clock.tick(60)
      self._update_screen() 
      self._check_events()
      if self._check_mouse_click():
        if not self.cards_up:
          mouse_pos = pygame.mouse.get_pos()
          choice = self.cards._get_selected_card(mouse_pos)
          #print(f"choice: {choice}")
          if choice is not None:
            self.win_or_lose = self.cards._flip_cards(choice)
            self.cards_up = True
            if self.win_or_lose:
              self.win_button.append(Button(self, "You Win", random.randint(200, 500), random.randint(200,500)))
            #  self.win_button.draw()
            #  self.win_button.move()
        else: 
          self.win_or_lose = False
          pygame.event.post(pygame.event.Event(RESET_CARD_EVENT))
      pygame.display.update()
    print("out of loop")
    pygame.quit()
    sys.exit()

  def _check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.game_active = False
      if event.type == RESET_CARD_EVENT: 
        self.cards_up = False
        self.cards._reset_cards()
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

  def _check_mouse_click(self): 
    if not pygame.mouse.get_pressed()[0] and self.mouse_clicked:
        self.mouse_clicked = False
        return True  # Released this frame
    elif pygame.mouse.get_pressed()[0]:
        self.mouse_clicked = True  # Still holding
    return False

  

def main():
  game = Game()
  game.game_loop()
  return 
    
if __name__ == '__main__':
  main()