import pygame
import os

import aliens
from helpers import alien
from helpers import shield
from helpers import laser
from helpers import asteroid

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
result = ['']
asteroids = []

def draw_result(text):
  text = RESULT_FONT.render(text, 1, (255, 255, 255))
  surface = pygame.display.get_surface()
  rect = pygame.Rect(
    WIDTH / 2 - text.get_width() / 2 - 30,
    HEIGHT / 2 - text.get_height() / 2 - 30,
    text.get_width() + 60,
    text.get_height() + 60
  )
  surface.fill((0, 128, 0), rect)
  WINDOW.blit(
    text,
    (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2)
  )
  result[0] = text
  pygame.display.update()
  pygame.time.delay(5000)

def draw_window():
  WINDOW.blit(pygame.transform.scale(BACKGROUND, (800, 600)), (0, 0))
  for idx, an_alien in enumerate(aliens.aliens):
    if aliens.alien_coordinates2[idx]['type'] == 1:
      WINDOW.blit(alien.get_alien1(current[0]), (an_alien.x, an_alien.y))
    elif aliens.alien_coordinates2[idx]['type'] == 2:
      WINDOW.blit(alien.get_alien2(current[0]), (an_alien.x, an_alien.y))
    else:
      WINDOW.blit(alien.get_alien3(current[0]), (an_alien.x, an_alien.y))
  for i in range(4):
    if shield_images[i] <= 5:
      WINDOW.blit(shield.get_shield(shield_images[i]), (83 + 200 * i, 500))
  if (laser_image[0] <= 6):
    WINDOW.blit(
      laser.get_laser(laser_image[0]),
      (laser.laser_rect.x, laser.laser_rect.y)
    )
  for an_asteroid in asteroids:
    WINDOW.blit(asteroid.get_asteroid(), (an_asteroid.x, an_asteroid.y))
  for shot in shots:
    pygame.draw.rect(WINDOW, (255, 0, 0), shot)
  for shot in alien_shots:
    pygame.draw.rect(WINDOW, (255, 165, 0), shot)
  for an_alien in aliens.aliens:
    if an_alien.y == 240:
      pygame.draw.line(
        WINDOW, 
        (255, 0, 0),
        [an_alien.x + 40, an_alien.y + 60], 
        [laser.laser_rect.x + 20, laser.laser_rect.y]
      )
  pygame.display.update()
