import pygame
import random

def get_random_shot(range: int, shots: list, aliens: list):
  random_number = int(random.random() * range)
  current_alien = aliens[random_number]
  shot = pygame.Rect(
    current_alien.x + current_alien.width / 2,
    current_alien.y + current_alien.height,
    7,
    14,
  )
  shots.append(shot)
