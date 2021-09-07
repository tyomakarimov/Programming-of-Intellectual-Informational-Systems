import pygame

shields = []

for i in range(4):
  shield = pygame.Rect(83 + 200 * i, 500, 54, 40)
  shields.append(shield)
