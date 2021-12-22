import pygame

shields = []

shields_coordinates = [
  { 'x': 30, 'y': 480 },
  { 'x': 90, 'y': 480 },
  { 'x': 150, 'y': 480 },
  { 'x': 210, 'y': 480 },
  { 'x': 270, 'y': 480 },
  { 'x': 330, 'y': 480 },
  { 'x': 390, 'y': 480 },
  { 'x': 450, 'y': 480 },
  { 'x': 510, 'y': 480 },
  { 'x': 570, 'y': 480 },
]

for coordinates in shields_coordinates:
  shield = pygame.Rect(coordinates['x'], coordinates['y'], 30, 30)
  shields.append(shield)
