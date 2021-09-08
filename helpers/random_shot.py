import pygame
import random
import sys

sys.path.append("..")

import aliens

def get_random_shot(range: int, shots: list):
  random_number = int(random.random() * range)
  current_alien = aliens.aliens[random_number]
  shot = pygame.Rect(
    current_alien.x + current_alien.width / 2,
    current_alien.y + current_alien.height,
    5,
    10,
  )
  shots.append(shot)
