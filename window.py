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
from BFS import BFS
from DFS import DFS
from UCS import UCS

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
algorithms = [BFS, DFS, UCS]
current_algorithm = [0]
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
      (laser.laser_rect.x, laser.laser_rect.y)
    )
  for shot in shots:
    pygame.draw.rect(WINDOW, (255, 0, 0), shot)
  for shot in alien_shots:
    pygame.draw.rect(WINDOW, (255, 165, 0), shot)
  pygame.display.flip()
  pygame.display.update()

def show_path(i, current_algorithm, changed):
  curr = current_algorithm[0]
  if changed or i % 60 == 0:
    matrix = the_matrix.generate_matrix()
    aliens = []
    laser = []
    for idx1, j in enumerate(matrix):
      for idx2, k in enumerate(j):
        if k == 2:
          aliens.append(the_neighbours.get_element(idx1, idx2))
        if k == 3:
          laser.append(the_neighbours.get_element(idx1, idx2))
    a_laser = laser[0]
    times = []
    for idx, an_alien in enumerate(aliens):
      start_time1 = time.time()
      the_path = algorithms[curr](an_alien, a_laser)
      times.append(time.time() - start_time1)
      previous_paths[idx] = the_path
    the_time = round(sum(times) / len(times), 7)
    func_name = algorithms[curr].__name__
    print('Current algorithm =>', f'{func_name},', 'Execution time:', the_time)
  for prev_path in previous_paths:
    path.draw_path(WINDOW, prev_path)
  pygame.display.flip()
  pygame.display.update()
