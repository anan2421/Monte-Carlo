import pygame 
import os 
WIDTH, HEIGHT = 1280, 720
CARD_WIDTH = int(HEIGHT/5) #Set card width relative to window height
CARD_HEIGHT = int(CARD_WIDTH * 16/9) #Maintain aspect ratio of card
X_SPACING = 20 #small spacer between cards
Y_SPACING = 50

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monte Carlo")
FPS = 60

BACKGROUND = pygame.image.load(os.path.join('Assets', 'background.png'))
CARD_BACK = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'card_back.png')), (CARD_WIDTH, CARD_HEIGHT))
QUEEN = pygame.transform.scale(pygame.image.load(os.path.join('Assets','queen_of_hearts.png')), (CARD_WIDTH, CARD_HEIGHT))
ACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets','ace_of_hearts.png')), (CARD_WIDTH, CARD_HEIGHT))

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

def play_again():
  font = pygame.font.SysFont(None, 48)
  small_font = pygame.font.SysFont(None, 36)
  #Button rect
  #yes_button = pygame.draw.rect(WINDOW, (255,255,0), (CARD_HEIGHT//5, CARD_WIDTH//5),0)
  #no_button = pygame.draw.rect(WINDOW, (255,255,0), (CARD_HEIGHT//5, CARD_WIDTH//5),0)
  continue_text = font.render("Continue?", True, (0,0,0))
  yes_text = small_font.render("Yes!!!", True, (0,0,0))
  no_text = small_font.render("No???", True, (0,0,0))
  #Draw continue and yes/no
  x_center = WIDTH//2 
  y_center = HEIGHT//2 + CARD_HEIGHT//2 + Y_SPACING
  WINDOW.blit(continue_text, (x_center - CARD_WIDTH/2, y_center))
  WINDOW.blit(yes_text, (x_center - CARD_WIDTH/2, y_center+Y_SPACING))
  WINDOW.blit(no_text, (x_center + CARD_WIDTH/2, y_center + Y_SPACING))
  #rect1 = pygame.Rect(left=, top=, width=, height=)
  # Create rects for collision detection
  button_hit_boxes =[]
  button_hit_boxes.append(yes_text.get_rect(topleft=(x_center - CARD_WIDTH/2, y_center + Y_SPACING)))
  button_hit_boxes.append(yes_text.get_rect(topleft=(x_center + CARD_WIDTH/2, y_center+ Y_SPACING)))
  pygame.display.update()
  return button_hit_boxes

def main():
  pygame.init()
  clock = pygame.time.Clock()
  cards_hit_box = draw_window()
  running = True
  game_state = ['bet', 'start', 'gameover']
  state = game_state[0]
  while running: 
    clock.tick(FPS)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
        pygame.quit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if state == game_state[0]:
          mouse_pos = pygame.mouse.get_pos()
          get_selected_card(mouse_pos, cards_hit_box)        
          #change game-state
          state = game_state[2]
          pygame.time.delay(1000)
        if state == game_state[2]:
          cards_hit_box= []
          cards_hit_box = play_again()
          mouse_pos = pygame.mouse.get_pos()
          for i, hit_box in enumerate(cards_hit_box): 
            if hit_box.collidepoint(mouse_pos):
              print(f"Option {i+1} clicked")
              print(f'this is new')
if __name__ == '__main__':
  main()