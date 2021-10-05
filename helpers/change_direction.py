def change_current_direction(move_left: bool, aliens: list, coordinates):
  if len(aliens) == 0:
    return
  x_positions = []
  y_positions = []
  for alien in aliens:
    x_positions.append(alien.x)
    y_positions.append(alien.y)
  min_x = min(x_positions)
  max_x = max(x_positions)
  max_y = max(y_positions)
  if min_x <= 1:
    move_left = False
    for alien in aliens:
      alien.y += 30
    for value in coordinates:
      value['y'] += 30
  if max_x >= 569:
    move_left = True
  for alien in aliens:
    if move_left:
      alien.x -= 30
    else:
      alien.x += 30
  if move_left:
    for value in coordinates:
      value['x'] -= 30
  else:
    for value in coordinates:
      value['x'] += 30
  return move_left, max_y
