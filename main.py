import pygame

from window import *
import shields
from helpers import laser_shots
from helpers import the_alien_shots
from helpers import random_shot
from helpers import current_position

FPS = 60

def main():
  clock = pygame.time.Clock()
  i = 0
  run = True
  while run:
    clock.tick(FPS)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP or event.key == pygame.K_w:
          print('hey')
          shot = pygame.Rect(
            laser.laser_rect.x + laser.laser_rect.width / 2,
            laser.laser_rect.y, 
            5,
            10
          )
          shots.append(shot)
    keys_pressed = pygame.key.get_pressed()
    if (
      keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]
    ) and laser.laser_rect.x - 3 > 0:
      laser.laser_rect.x -= 3
    if (
      keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]
    ) and laser.laser_rect.x + laser.laser_rect.width + 10 < WIDTH:
      laser.laser_rect.x += 3
    laser_shots.handle_laser_shots(
      shots,
      aliens.aliens,
      shields.shields,
      shield_images
    )
    the_alien_shots.handle_alien_shots(
      laser.laser_rect,
      alien_shots,
      laser_image,
      shields.shields,
      shield_images
    )
    draw_window()

    if (i % 30 == 0) and len(aliens.aliens) > 0:
      random_shot.get_random_shot(len(aliens.aliens), alien_shots)
      current_position.change_current_position(current)
      print(current[0])
    i += 1
  pygame.quit()

if __name__ == '__main__':
  main()
