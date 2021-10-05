import shields
import aliens
from helpers import laser

def check_shield(x: int, y: int):
  for shield in shields.shields_coordinates:
    if (shield['x'] == x * 30 and shield['y'] == y * 30):
      return True
  return False

def check_alien(x: int, y: int):
  for alien in aliens.alien_coordinates:
    if (alien['x'] == x * 30 and alien['y'] == y * 30):
      return True
  return False

def check_laser(x: int, y: int):
  if laser.laser_coordinates['x'] == x * 30 and laser.laser_coordinates['y'] == y * 30:
    return True
  return False

def generate_matrix():
  matrix = []
  for i in range(20):
    row = []
    for j in range(20):
      if check_shield(i, j):
        row.append(1)
      elif check_alien(i, j):
        row.append(2)
      elif check_laser(i, j):
        row.append(3)
      else:
        row.append(0)
    matrix.append(row)
  zipped_rows = zip(*matrix)
  transpose_matrix = [list(row) for row in zipped_rows]
  return transpose_matrix

generate_matrix()
