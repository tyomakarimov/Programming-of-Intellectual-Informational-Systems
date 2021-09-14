import pygame
import os
import random

def get_asteroid_rect(asteroids: list):
  random_number = int(random.random() * 25) + 10
  asteroids.append(pygame.Rect(random_number * 20, 0, 8, 100))

def get_asteroid():
  return pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'asteroid.png')), (8, 100)
  )
