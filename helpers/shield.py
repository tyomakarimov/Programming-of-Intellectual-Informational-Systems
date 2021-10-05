import pygame
import os


def get_shield(current: int):
  return pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', f'shield{current}.png')), (30, 30)
  )
