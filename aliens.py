import pygame

alien_coordinates = [
  { 'x': 150, 'y': 60, 'type': 'random', 'number': 1 },
  { 'x': 210, 'y': 60, 'type': 'random', 'number': 2 },
  { 'x': 270, 'y': 60, 'type': 'random', 'number': 3 },
  { 'x': 330, 'y': 60, 'type': 'random', 'number': 4 },
  { 'x': 390, 'y': 60, 'type': 'random', 'number': 5 },

  { 'x': 150, 'y': 120, 'type': 'random', 'number': 6 },
  { 'x': 210, 'y': 120, 'type': 'random', 'number': 7 },
  { 'x': 270, 'y': 120, 'type': 'random', 'number': 8 },
  { 'x': 330, 'y': 120, 'type': 'search', 'number': 9 },
  { 'x': 390, 'y': 120, 'type': 'search', 'number': 10 },

  { 'x': 150, 'y': 180, 'type': 'random', 'number': 11 },
  { 'x': 210, 'y': 180, 'type': 'random', 'number': 12 },
  { 'x': 270, 'y': 180, 'type': 'search', 'number': 13 },
  { 'x': 330, 'y': 180, 'type': 'search', 'number': 14 },
  { 'x': 390, 'y': 180, 'type': 'random', 'number': 15 },
]

aliens = []

for coordinates in alien_coordinates:
  alien_rect = pygame.Rect(coordinates['x'], coordinates['y'], 30, 30)
  aliens.append(alien_rect)
