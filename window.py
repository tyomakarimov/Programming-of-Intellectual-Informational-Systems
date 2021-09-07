import pygame
import os

pygame.display.set_caption('Space Invaders')

WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.image.load(os.path.join('Assets', 'bg.jpg'))

def draw_window():
  WINDOW.blit(pygame.transform.scale(BACKGROUND, (800, 600)), (0, 0))
  pygame.display.update()
