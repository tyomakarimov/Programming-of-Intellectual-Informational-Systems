import pygame

from window import *
import shields
from helpers import laser_shots
from helpers import the_alien_shots
from helpers import the_asteroids
from helpers import random_shot
from helpers import current_position
from helpers import change_direction

FPS = 60

def main():
  clock = pygame.time.Clock()
  i = 0
  move_left = True
  run = True
  while run:
    clock.tick(FPS)
    if (result[0]):
      break
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP or event.key == pygame.K_w:
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
      laser.laser_rect.x -= 30
    if (
      keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]
    ) and laser.laser_rect.x + laser.laser_rect.width + 10 < WIDTH:
      laser.laser_rect.x += 30
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
    the_asteroids.handle_asteroids(
      laser.laser_rect,
      asteroids,
      laser_image,
      shields.shields,
      shield_images
    )
    draw_window()
    if len(aliens.aliens) == 0:
      draw_result('You have won!!!')
    if laser_image[0] > 6:
      draw_result('You have lost.')
    if (i % 60 == 0) and len(aliens.aliens) > 0:
      random_shot.get_random_shot(len(aliens.aliens), alien_shots, aliens.aliens)
      current_position.change_current_position(current)
      move_left_value, max_y = change_direction.change_current_direction(move_left, aliens.aliens)
      move_left = move_left_value
      if max_y > 440:
        draw_result('You have lost.')
    i += 1
  result[0] = ''
  pygame.quit()

if __name__ == '__main__':
  main()
