import pygame
import os

laser_rect = pygame.Rect(500, 550, 32, 20)

def get_laser(current: int):
  return pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', f'laser{current}.png')), (40, 25)
  )
