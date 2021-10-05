import pygame

shields = []

shields_coordinates = [
  { 'x': 30, 'y': 480 },
  { 'x': 90, 'y': 480 },
  { 'x': 150, 'y': 480 },
  { 'x': 210, 'y': 480 },
  { 'x': 210, 'y': 450 },
  { 'x': 270, 'y': 480 },
  { 'x': 330, 'y': 480 },
  { 'x': 390, 'y': 480 },
  { 'x': 450, 'y': 480 },
  { 'x': 510, 'y': 480 },
  { 'x': 570, 'y': 480 },
  { 'x': 60, 'y': 450 },
  { 'x': 150, 'y': 450 },
  { 'x': 240, 'y': 450 },
  { 'x': 420, 'y': 450 },
  { 'x': 30, 'y': 570 },
  { 'x': 90, 'y': 570 },
  { 'x': 150, 'y': 570 },
  { 'x': 210, 'y': 570 },
  { 'x': 270, 'y': 570 },
  { 'x': 330, 'y': 570 },
  { 'x': 390, 'y': 570 },
  { 'x': 450, 'y': 570 },
  { 'x': 510, 'y': 570 },
  { 'x': 60, 'y': 420 },
  { 'x': 90, 'y': 420 },
  { 'x': 150, 'y': 420 },
  { 'x': 180, 'y': 420 },
  { 'x': 240, 'y': 420 },
  { 'x': 330, 'y': 420 },
]

for coordinates in shields_coordinates:
  shield = pygame.Rect(coordinates['x'], coordinates['y'], 30, 30)
  shields.append(shield)
