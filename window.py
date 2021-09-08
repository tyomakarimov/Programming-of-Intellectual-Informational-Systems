import pygame
import os

import aliens
from helpers import alien
from helpers import shield
from helpers import laser

pygame.font.init()
pygame.display.set_caption('Space Invaders')

WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.image.load(os.path.join('Assets', 'bg.jpg'))
RESULT_FONT = pygame.font.SysFont('roboto', 80)

shield_images = [0, 0, 0, 0]
laser_image = [0]

shots = []
alien_shots = []
current = [0]

def draw_window():
  WINDOW.blit(pygame.transform.scale(BACKGROUND, (800, 600)), (0, 0))
  for idx, an_alien in enumerate(aliens.aliens):
    if aliens.alien_coordinates[idx]['type'] == 1:
      WINDOW.blit(alien.get_alien1(current[0]), (an_alien.x, an_alien.y))
    elif aliens.alien_coordinates[idx]['type'] == 2:
      WINDOW.blit(alien.get_alien2(current[0]), (an_alien.x, an_alien.y))
    else:
      WINDOW.blit(alien.get_alien3(current[0]), (an_alien.x, an_alien.y))
  for i in range(4):
    if shield_images[i] <= 5:
      WINDOW.blit(shield.get_shield(shield_images[i]), (83 + 200 * i, 500))
  if (laser_image[0] <= 6):
    WINDOW.blit(laser.get_laser(laser_image[0]), (laser.laser_rect.x, laser.laser_rect.y))
  for shot in shots:
    pygame.draw.rect(WINDOW, (255, 0, 0), shot)
  for shot in alien_shots:
    pygame.draw.rect(WINDOW, (255, 165, 0), shot)
  pygame.display.update()
