import pygame
import os
import time

import aliens
from helpers import alien
from helpers import shield
from helpers import laser
import shields
import path
import the_matrix
from helpers import the_neighbours
from A_star import A_star
from helpers import the_shortest_path
import run_from_shots

pygame.font.init()
pygame.display.set_caption('Space Invaders')

WIDTH, HEIGHT = 600, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.image.load(os.path.join('Assets', 'bg.jpg'))
RESULT_FONT = pygame.font.SysFont('roboto', 80)

shield_images = []

for i in range(len(shields.shields_coordinates)):
  shield_images.append(0)

laser_image = [0]

shots = []
alien_shots = []
current = [0]
result = ['']
asteroids = []
algorithms = [A_star]
current_algorithm = [0]
current_index = [0]
previous_paths = []

for i in range(15): 
  previous_paths.append(0)

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
    WINDOW.blit(alien.get_alien1(current[0]), (an_alien.x, an_alien.y))
  for i in range(len(shields.shields_coordinates)):
    if shield_images[i] <= 5:
      WINDOW.blit(shield.get_shield(
        shield_images[i]),
        (shields.shields_coordinates[i]['x'], shields.shields_coordinates[i]['y'])
      )
  if (laser_image[0] <= 6):
    WINDOW.blit(
      laser.get_laser(laser_image[0]),
      (laser.laser_coordinates['x'], laser.laser_coordinates['y'])
    )
  for shot in shots:
    pygame.draw.rect(WINDOW, (255, 0, 0), shot)
  for shot in alien_shots:
    pygame.draw.rect(WINDOW, (255, 165, 0), shot)
  pygame.display.flip()
  pygame.display.update()

alien_coordinates = aliens.alien_coordinates

def show_path(i, current_algorithm, changed, move_left):
  curr = current_algorithm[0]
  current_paths = []
  if changed or i % 60 == 0:
    matrix = the_matrix.generate_matrix()
    aliens = []
    the_laser = []
    for idx1, j in enumerate(matrix):
      for idx2, k in enumerate(j):
        if k == 2:
          aliens.append(the_neighbours.get_element(idx1, idx2))
        if k == 3:
          the_laser.append(the_neighbours.get_element(idx1, idx2))
    a_laser = the_laser[0]
    times = []
    for idx, an_alien in enumerate(aliens):
      start_time1 = time.time()
      the_path = algorithms[curr](an_alien, a_laser)
      current_paths.append({ an_alien: len(the_path) })
      times.append(time.time() - start_time1)
      previous_paths[idx] = the_path
    # the_time = round(sum(times) / len(times), 7)
    # func_name = algorithms[curr].__name__
    # print('Current algorithm =>', f'{func_name},', 'Execution time:', the_time)
  if len(current_paths):
    shortest_path, index = the_shortest_path.get_the_shortest_path(current_paths)
    current_index[0] = index
    the_x = the_neighbours.get_element_indeces(shortest_path)[1]
    if not changed:
      laser.laser_coordinates['x'] = the_x * 30
      laser.laser_rect.x = the_x * 30
      shot = pygame.Rect(
        laser.laser_rect.x + laser.laser_rect.width / 2,
        laser.laser_rect.y,
        5,
        10
      )
      shots.append(shot)
    path.draw_path(WINDOW, previous_paths[current_index[0]])
    # run_from_shots.run_from_shots(shots, aliens, shields.shields, move_left)
    run_from_shots.run_from_shots(shots, alien_coordinates, shields.shields)
  pygame.display.flip()
  pygame.display.update()
