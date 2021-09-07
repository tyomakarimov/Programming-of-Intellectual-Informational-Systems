def get_ends(aliens: list):
  if len(aliens) == 0:
    return
  x_positions = []
  y_positions = []
  for alien in aliens:
    x_positions.append(alien.x)
    y_positions.append(alien.y)
  min_x_value = min(x_positions)
  max_x_value = max(x_positions)
  max_y_value = max(y_positions)
  return [min_x_value, max_x_value, max_y_value]
