import pygame
from helpers import the_neighbours

def draw_path(window, path):
  for i in range(len((path)) - 1):
    i1 = the_neighbours.get_element_indeces(path[i])
    i2 = the_neighbours.get_element_indeces(path[i + 1])
    pygame.draw.line(
      window,
      (255, 0, 0),
      (i1[1] * 30 + 15, i1[0] * 30), (i2[1] * 30 + 15, i2[0] * 30),
      2
    )
