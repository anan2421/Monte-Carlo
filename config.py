#Config file contain all Global variables and packages 
import pygame
import os 
import random 

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