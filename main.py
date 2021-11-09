import pygame

from window import *
import shields
import aliens
from helpers import laser_shots
from helpers import the_alien_shots
from helpers import the_asteroids
from helpers import random_shot
from helpers import current_position
from helpers import change_direction
from constants import *
from csv_writer import write_to_scv

FPS = 60
result = [0, 0, 0, 0, 0]

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
        if (
          event.key == pygame.K_LEFT or event.key == pygame.K_a
        ) and laser.laser_rect.x - 3 > 0:
          laser.laser_rect.x -= 30
          laser.laser_coordinates['x'] -= 30
          show_path(i, current_algorithm, True, move_left)
        if (
          event.key == pygame.K_RIGHT or event.key == pygame.K_d
        ) and laser.laser_rect.x + laser.laser_rect.width + 10 < WIDTH:
          laser.laser_rect.x += 30
          laser.laser_coordinates['x'] += 30
          show_path(i, current_algorithm, True, move_left)
    laser_shots.handle_laser_shots(
      shots,
      aliens.aliens,
      shields.shields,
      shield_images,
      aliens.alien_coordinates,
      previous_paths
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
      score = ALIEN_VALUE * NUMBER_OF_ALIENS + (105 - LASER_VALUE * laser_image[0])
      player_health = TOTAL_HEALTH - laser_image[0] * HEALTH_LOST
      result[0] = 'True'
      result[2] = score
      result[3] = player_health
      result[4] = algorithms[current_algorithm[0]].__name__
      draw_result('You have won!!!')
    if laser_image[0] > 6:
      score = ALIEN_VALUE * (NUMBER_OF_ALIENS  - len(aliens.aliens))
      result[0] = 'False'
      result[2] = score
      result[3] = 0
      result[4] = algorithms[current_algorithm[0]].__name__
      draw_result('You have lost.')
    if (i % 60 == 0) and len(aliens.aliens) > 0:
      random_shot.get_random_shot(len(aliens.aliens), alien_shots, aliens.aliens)
      current_position.change_current_position(current)
      move_left_value, max_y = change_direction.change_current_direction(
        move_left,
        aliens.aliens,
        aliens.alien_coordinates
      )
      move_left = move_left_value
      if max_y > 440:
        score = ALIEN_VALUE * NUMBER_OF_ALIENS + (105 - LASER_VALUE * laser_image[0])
        player_health = TOTAL_HEALTH - laser_image[0] * HEALTH_LOST
        result[0] = 'False'
        result[2] = score
        result[3] = player_health
        result[4] = algorithms[current_algorithm[0]].__name__
        draw_result('You have lost.')
    show_path(i, current_algorithm, False, move_left)
    i += 1
  result[0] = ''
  pygame.quit()

if __name__ == '__main__':
  start_time = time.time()
  main()
  finish_time = time.time() - start_time - 5
  result[1] = finish_time
  write_to_scv(result)
