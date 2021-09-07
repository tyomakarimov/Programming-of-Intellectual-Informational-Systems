import pygame
import os

import aliens
from helpers import alien

pygame.font.init()
pygame.display.set_caption('Space Invaders')

WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.image.load(os.path.join('Assets', 'bg.jpg'))
RESULT_FONT = pygame.font.SysFont('roboto', 80)

def draw_window():
  WINDOW.blit(pygame.transform.scale(BACKGROUND, (800, 600)), (0, 0))
  for idx, an_alien in enumerate(aliens.aliens):
    if aliens.alien_coordinates[idx]['type'] == 1:
      WINDOW.blit(alien.get_alien1(0), (an_alien.x, an_alien.y))
    elif aliens.alien_coordinates[idx]['type'] == 2:
      WINDOW.blit(alien.get_alien2(0), (an_alien.x, an_alien.y))
    else:
      WINDOW.blit(alien.get_alien3(0), (an_alien.x, an_alien.y))
  pygame.display.update()
