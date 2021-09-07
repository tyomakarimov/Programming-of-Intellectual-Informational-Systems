import pygame
import os

alien_states1 = ['alien.png', 'alien1.png']
alien_states2 = ['alien2.png', 'alien3.png']
alien_states3 = ['alien4.png', 'alien5.png']


def get_alien1(current: int):
  return pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', alien_states1[current])), (40, 40)
  )


def get_alien2(current: int):
  return pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', alien_states2[current])), (40, 40)
  )


def get_alien3(current: int):
  return pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', alien_states3[current])), (40, 40)
  )
