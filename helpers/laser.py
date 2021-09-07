import pygame
import os


def get_laser(current: int):
  return pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', f'laser{current}.png')), (40, 25)
  )
