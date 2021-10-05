import pygame

alien_coordinates = [
  { 'x': 150, 'y': 60 },
  { 'x': 210, 'y': 60 },
  { 'x': 270, 'y': 60 },
  { 'x': 330, 'y': 60 },
  { 'x': 390, 'y': 60 },

  { 'x': 150, 'y': 120 },
  { 'x': 210, 'y': 120 },
  { 'x': 270, 'y': 120 },
  { 'x': 330, 'y': 120 },
  { 'x': 390, 'y': 120 },


  { 'x': 150, 'y': 180 },
  { 'x': 210, 'y': 180 },
  { 'x': 270, 'y': 180 },
  { 'x': 330, 'y': 180 },
  { 'x': 390, 'y': 180 },
]

aliens = []

for coordinates in alien_coordinates:
  alien_rect = pygame.Rect(coordinates['x'], coordinates['y'], 30, 30)
  aliens.append(alien_rect)
