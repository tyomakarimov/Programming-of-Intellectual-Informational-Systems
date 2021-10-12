import pygame
import os

laser_coordinates = { 'x': 480, 'y': 540 }

laser_rect = pygame.Rect(laser_coordinates['x'], laser_coordinates['y'], 30, 30)

def get_laser(current: int):
  return pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', f'laser{current}.png')), (30, 19)
  )
