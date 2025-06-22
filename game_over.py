from config import *

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